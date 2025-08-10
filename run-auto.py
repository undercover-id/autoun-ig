import hashlib
from nacl.secret import SecretBox


def run_bf(src: str) -> str:
    tape = [0] * 30000
    p = 0
    output_chars = []
    pc = 0
    src_len = len(src)
    
    jump = {}
    stack = []
    for i, c in enumerate(src):
        if c == '[':
            stack.append(i)
        elif c == ']':
            if not stack:
                raise ValueError(run_bf(ERRORHEHE))
            j = stack.pop()
            jump[i] = j
            jump[j] = i
    if stack:
        raise ValueError(run_bf(ERRORHEHE))
    
    while pc < src_len:
        c = src[pc]
        if c == '>':
            p += 1
            if p >= len(tape):
                tape.extend([0] * 10000)
        elif c == '<':
            p = p - 1 if p > 0 else 0
        elif c == '+':
            tape[p] = (tape[p] + 1) & 0xFF
        elif c == '-':
            tape[p] = (tape[p] - 1) & 0xFF
        elif c == '.':
            output_chars.append(chr(tape[p]))
        elif c == ',':
            tape[p] = 0
        elif c == '[':
            if tape[p] == 0:
                pc = jump[pc]
        elif c == ']':
            if tape[p] != 0:
                pc = jump[pc]
        pc += 1
    return ''.join(output_chars)


ERRORHEHE = (
    "[-]" + "+"*116 + "."
    + "[-]" + "+"*101 + "."
    + "[-]" + "+"*114 + "."
    + "[-]" + "+"*106 + "."
    + "[-]" + "+"*97 + "."
    + "[-]" + "+"*100 + "."
    + "[-]" + "+"*105 + "."
    + "[-]" + "+"*32 + "."
    + "[-]" + "+"*101 + "."
    + "[-]" + "+"*114 + "."
    + "[-]" + "+"*111 + "."
    + "[-]" + "+"*114 + "."
    + "[-]" + "+"*32 + "."
    + "[-]" + "+"*112 + "."
    + "[-]" + "+"*97 + "."
    + "[-]" + "+"*100 + "."
    + "[-]" + "+"*97 + "."
    + "[-]" + "+"*32 + "."
    + "[-]" + "+"*107 + "."
    + "[-]" + "+"*111 + "."
    + "[-]" + "+"*100 + "."
    + "[-]" + "+"*101 + "."
)


HEHE = (
    "[-]" + "+"*77 + "."
    + "[-]" + "+"*97 + "."
    + "[-]" + "+"*115 + "."
    + "[-]" + "+"*117 + "."
    + "[-]" + "+"*107 + "."
    + "[-]" + "+"*107 + "."
    + "[-]" + "+"*97 + "."
    + "[-]" + "+"*110 + "."
    + "[-]" + "+"*32 + "."
    + "[-]" + "+"*112 + "."
    + "[-]" + "+"*97 + "."
    + "[-]" + "+"*115 + "."
    + "[-]" + "+"*115 + "."
    + "[-]" + "+"*119 + "."
    + "[-]" + "+"*111 + "."
    + "[-]" + "+"*114 + "."
    + "[-]" + "+"*100 + "."
    + "[-]" + "+"*58 + "."
    + "[-]" + "+"*32 + "."
)


HEHEHE = (
    "[-]" + "+"*118 + "."
    + "[-]" + "+"*105 + "."
    + "[-]" + "+"*99 + "."
    + "[-]" + "+"*107 + "."
    + "[-]" + "+"*46 + "."
    + "[-]" + "+"*98 + "."
    + "[-]" + "+"*105 + "."
    + "[-]" + "+"*110 + "."
)


HEHEHEHE = (
    "[-]" + "+"*114 + "."
    + "[-]" + "+"*98 + "."
)


pw = input(run_bf(HEHE))
key = hashlib.sha256(pw.encode()).digest()[:32]
box = SecretBox(key)
with open(run_bf(HEHEHE), run_bf(HEHEHEHE)) as f:
    data = f.read()
code = box.decrypt(data)
exec(code.decode())
