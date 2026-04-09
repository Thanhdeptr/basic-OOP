import sys

# If you run with: python zombie_apocalypse_oop.py path/to/input.txt
# (or visualize_game.py input.txt), lines are read from that file instead of stdin.
_INPUT_LINES: list[str] | None = None
_input_line_index: int = 0


def reset_input_from_argv() -> None:
    global _INPUT_LINES, _input_line_index
    _input_line_index = 0
    if len(sys.argv) > 1:
        path = sys.argv[1]
        with open(path, encoding="utf-8") as f:
            _INPUT_LINES = [line.rstrip("\n\r") for line in f]
        print(f"[Input] Doc tu file: {path} ({len(_INPUT_LINES)} dong)")
    else:
        _INPUT_LINES = None


def read_line(prompt: str = "") -> str:
    global _input_line_index
    if _INPUT_LINES is not None:
        if _input_line_index >= len(_INPUT_LINES):
            raise EOFError(
                f"Het du lieu file input (can them dong sau dong {_input_line_index})"
            )
        if prompt:
            print(prompt, end="", flush=True)
        line = _INPUT_LINES[_input_line_index]
        _input_line_index += 1
        if prompt:
            print(line)
        return line
    return input(prompt) if prompt else input()


def is_file_input_mode() -> bool:
    return _INPUT_LINES is not None
