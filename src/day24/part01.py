from __future__ import annotations

import operator
import time
from abc import abstractproperty, abstractmethod, ABC
from enum import Enum
from itertools import cycle, repeat, count, combinations_with_replacement, product
from typing import Callable, Generator

from attr import dataclass

from src.day22.common import get_final_on_volume
from src.shared import load_text_file


class InstructionType(Enum):
    INPUT = "inp"
    ADD = "add"
    SUBTRACT = "sub"
    MULTIPLY = "mul"
    DIVIDE = "div"
    MODULO = "mod"
    EQUALS = "eql"


class RegisterIndex(Enum):
    W = 0
    X = 1
    Y = 2
    Z = 3

Registers = tuple[int, int, int, int]


@dataclass
class Instruction(ABC):
    operand1_and_output: RegisterIndex
    operand2: RegisterIndex | int | None = None

    @property
    @abstractmethod
    def type(self) -> InstructionType:
        ...

    @abstractmethod
    def perform(self, input_registers: Registers, inputs: list[int]) -> Registers:
        ...

    def _value1(self, input_registers: Registers) -> int:
        return input_registers[self.operand1_and_output.value]

    def _value2(self, input_registers: Registers) -> int:
        if self.operand2 is None:
            raise Exception("cannot get value2, there is no operand2!")
        if isinstance(self.operand2, RegisterIndex):
            return input_registers[self.operand2.value]
        else:
            return self.operand2

    def _perform_arithmetic_operation(self, input_registers: Registers, operation: Callable[[int, int], int]) -> Registers:
        result = operation(self._value1(input_registers), self._value2(input_registers))

        output_idx = self.operand1_and_output.value
        output_registers = Registers(input_registers[:output_idx] + tuple([result]) + input_registers[output_idx + 1:])
        return output_registers

    @staticmethod
    def create(input_text: str) -> Instruction:
        parts = input_text.split(" ")
        type = parts[0]
        operand1 = RegisterIndex[parts[1].upper()]
        operand2: RegisterIndex | int | None = None
        if len(parts) > 2:
            if parts[2].strip("-").isnumeric():
                operand2 = int(parts[2])
            else:
                operand2 = RegisterIndex[parts[2].upper()]

        match type:
            case InstructionType.INPUT.value:
                return InputInstruction(operand1)
            case InstructionType.ADD.value:
                return AddInstruction(operand1, operand2)
            case InstructionType.SUBTRACT.value:
                return SubtractInstruction(operand1, operand2)
            case InstructionType.MULTIPLY.value:
                return MultiplyInstruction(operand1, operand2)
            case InstructionType.DIVIDE.value:
                return DivideInstruction(operand1, operand2)
            case InstructionType.MODULO.value:
                return ModuloInstruction(operand1, operand2)
            case InstructionType.EQUALS.value:
                return EqualsInstruction(operand1, operand2)


class InputInstruction(Instruction):
    def type(self):
        return InstructionType.INPUT

    def perform(self, input_registers: Registers, inputs: list[int]) -> Registers:
        input_value = inputs.pop(0)
        output_idx = self.operand1_and_output.value
        output_registers = Registers(input_registers[:output_idx] + tuple([input_value]) + input_registers[output_idx + 1:])
        return output_registers


class AddInstruction(Instruction):
    def type(self):
        return InstructionType.ADD

    def perform(self, input_registers: Registers, inputs: list[int]) -> Registers:
        return self._perform_arithmetic_operation(input_registers, operator.add)


class SubtractInstruction(Instruction):
    def type(self):
        return InstructionType.SUBTRACT

    def perform(self, input_registers: Registers, inputs: list[int]) -> Registers:
        return self._perform_arithmetic_operation(input_registers, operator.sub)


class MultiplyInstruction(Instruction):
    def type(self):
        return InstructionType.MULTIPLY

    def perform(self, input_registers: Registers, inputs: list[int]) -> Registers:
        return self._perform_arithmetic_operation(input_registers, operator.mul)


class DivideInstruction(Instruction):
    def type(self):
        return InstructionType.DIVIDE

    def perform(self, input_registers: Registers, inputs: list[int]) -> Registers:
        return self._perform_arithmetic_operation(input_registers, operator.floordiv)


class ModuloInstruction(Instruction):
    def type(self):
        return InstructionType.MODULO

    def perform(self, input_registers: Registers, inputs: list[int]) -> Registers:
        return self._perform_arithmetic_operation(input_registers, operator.mod)


class EqualsInstruction(Instruction):
    def type(self):
        return InstructionType.EQUALS

    def perform(self, input_registers: Registers, inputs: list[int]) -> Registers:
        return self._perform_arithmetic_operation(input_registers, lambda a, b: 1 if a == b else 0)


@dataclass
class Computer:
    instructions: list[Instruction]
    registers: Registers = Registers([0, 0, 0, 0])

    def run(self, inputs: list[int]) -> bool:
        try:
            for instruction in self.instructions:
                self.registers = instruction.perform(self.registers, inputs)
            return True
        except Exception:
            return False

@dataclass
class App(ABC):
    computer: Computer

    @abstractmethod
    def _completed_successfully(self) -> bool:
        ...

    def run(self, inputs: list[int]):
        self.computer.run(inputs)
        return self._completed_successfully()


class MonadApp(App):
    def _completed_successfully(self) -> bool:
        return self.computer.registers[RegisterIndex.Z.value] == 0

    @staticmethod
    def input_generator(length: int) -> Generator[list[int]]:
        allowed_digits = list(range(9, 0, -1))
        number_generator = product(allowed_digits,repeat=length)
        while True:
            next_number = next(number_generator)
            yield list(next_number)


def load_instructions_from_file(file_name: str):
    lines = load_text_file(file_name)
    instructions: list[Instruction] = []
    for line in lines:
        instruction = Instruction.create(line)
        instructions.append(instruction)
    return instructions


def get_part_one_result(file_name: str):
    instructions = load_instructions_from_file(file_name)
    # input = [15]
    num_digits = 14
    computer = Computer(instructions)
    app = MonadApp(computer)
    generator = app.input_generator(num_digits)
    success = False
    while success is False:
        input = next(generator)
        success = app.run(input)
    return computer.registers





if __name__ == "__main__":
    start = time.time()
    result = get_part_one_result("src/day24/input.txt")
    end = time.time()

    print(f"Running Time: {end - start}")
    print(f"Result: {result}")
