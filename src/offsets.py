GADGET_OFFSETS = {
    "A YEAR OF SPRINGS": {
        "PS4": {
            # exec
            "add rsp, 0x1b8; ret": 0xE7DC1,
            "pop rax; ret": 0xC710E,
            "pop rcx; ret": 0x1151A3,
            "pop rdx; ret": 0x20B6FB,
            "pop rsi; ret": 0x9884B,
            "pop rdi; ret": 0xE2B93,
            "pop r8; ret": 0xC710D,
            "pop r9; ret": 0x68A7DF,
            "mov [rsi], rax; ret": 0x795C0A,
            "mov rsp, rbp; pop rbp; ret": 0x56AA,
            "push rbp; mov rbp, rsp; xor esi, esi; call [rdi + 0x130]": 0x3414C0,
            "add [r8 - 0x7d], rcx; ret": 0x752685,
            "ret": 0x42,
            "mov [rcx], rdx; ret": 0x7E9780,
            # libc
            "mov rsp, [rdi + 0x38]; pop rdi; ret": 0x26FFE,
            "mov rax, [rax]; ret": 0xB0057,
        }
    },
    "Arcade Spirits: The New Challengers": {
        "PS4": {
            # exec
            "add rsp, 0x1b8; ret": 0x856DF1,
            "pop rax; ret": 0xA60CD,
            "pop rcx; ret": 0xE6E03,
            "pop rdx; ret": 0x9C762,
            "pop rsi; ret": 0x153B1B,
            "pop rdi; ret": 0x57456,
            "pop r8; ret": 0x25BADF,
            "pop r9; ret": 0x6654CF,
            "mov [rsi], rax; ret": 0x7D528A,
            "mov rsp, rbp; pop rbp; ret": 0xC4,
            "push rbp; mov rbp, rsp; xor esi, esi; call [rdi + 0x130]": 0x2D6410,
            "add [r8 - 0x7d], rcx; ret": 0x72087E,
            "ret": 0x42,
            "mov [rcx], rdx; ret": 0x33A3DE,
            # libc
            "mov rsp, [rdi + 0x38]; pop rdi; ret": 0x26FFE,
            "mov rax, [rax]; ret": 0xB0057,
        },
        "PS5": {
            # exec
            "add rsp, 0x1b8; ret": 0x8774C6,
            "pop rax; ret": 0x5C52C,
            "pop rcx; ret": 0x7788B,
            "pop rdx; ret": 0x2BBF32,
            "pop rsi; ret": 0x83F82,
            "pop rdi; ret": 0x2FC0FD,
            "pop r8; ret": 0x804111,
            "mov [rsi], rax; ret": 0x7FE05A,
            "mov rsp, rbp; pop rbp; ret": 0x114,
            "push rbp; mov rbp, rsp; xor esi, esi; call [rdi + 0x130]": 0x38BC50,
            "add [r8 - 0x7d], rcx; ret": 0x7A3735,
            "ret": 0x32,
            "mov [rcx], rdx; ret": 0x8AB2C0,
            "mov r9, [rax+rsi+0x18]; xor eax, eax; mov [r8], r9; ret": 0x78D202,
            # libc
            "mov rsp, [rdi + 0x38]; pop rdi; ret": 0x3EB7E,
            "mov rax, [rax]; ret": 0x700D7,
        },
    },
    "One Night Stand": {
        "PS4": {
            # exec
            "ret 0x1b8": 0x44E8B8,
            "pop rax; ret": 0x16A95,
            "pop rcx; ret": 0x9E92E,
            "pop rdx; ret": 0x4FCD4,
            "pop rsi; ret": 0x9FBC1,
            "pop rdi; ret": 0x6AFCD,
            "pop r8; ret": 0x5B0562,
            "pop r9; ret": 0x43FCA5,
            "mov [rsi], rax; ret": 0x16417F,
            "mov rsp, rbp; pop rbp; ret": 0x5C7B4,
            "push rbp; mov rbp, rsp; xor esi, esi; call [rdi + 0x130]": 0x18BB30,
            "add [r8 - 0x7d], rcx; ret": 0x160435,
            "ret": 0x4C,
            "mov [rcx], rdx; ret": 0x1D149F,
            # libc
            "mov rsp, [rdi + 0x38]; pop rdi; ret": 0x338E2,
            "mov rax, [rax]; ret": 0x2DE0A,
        },
        "PS5": {
            # exec
            "add rsp, 0x1b8; ret": 0x187F86,
            "pop rax; ret": 0x5C31C,
            "pop rcx; ret": 0x7E584,
            "pop rdx; ret": 0x512D12,
            "pop rsi; ret": 0x5F72E,
            "pop rdi; ret": 0x75269,
            "pop r8; ret": 0x166F0C,
            "mov [rdi], rax; ret": 0x7D28A,
            "mov rsp, rbp; pop rbp; ret": 0x114,
            "push rbp; mov rbp, rsp; xor esi, esi; call [rdi + 0x130]": 0x3ED130,
            "add [r8 - 0x7d], rcx; ret": 0x80FFD5,
            "ret": 0x32,
            "mov [rcx], rdx; ret": 0x89ADA0,
            "mov r9, [rax+rsi+0x18]; xor eax, eax; mov [r8], r9; ret": 0x7F97B2,
            # libc
            "mov rsp, [rdi + 0x38]; pop rdi; ret": 0x3D10E,
            "mov rax, [rax]; ret": 0x13A3B,
        },
    },
    "Blind Men": {
        "PS4": {
            # exec
            "add rsp, 0x1b8; ret": 0x67F905,
            "pop rax; ret": 0x203D4,
            "pop rcx; ret": 0x918A3,
            "pop rdx; ret": 0x1B0052,
            "pop rsi; ret": 0x6FAA,
            "pop rdi; ret": 0x6B24,
            "pop r8; ret": 0x607BD2,
            "pop r9; ret": 0x464C18,
            "mov [rsi], rax; ret": 0x16787F,
            "mov rsp, rbp; pop rbp; ret": 0x5FD39,
            "push rbp; mov rbp, rsp; xor esi, esi; call [rdi + 0x130]": 0x18F2F0,
            "add [r8 - 0x7d], rcx; ret": 0x163B45,
            "ret": 0x4C,
            "mov [rcx], rdx; ret": 0x1D45AF,
            # libc
            "mov rsp, [rdi + 0x38]; pop rdi; ret": 0x295EE,
            "mov rax, [rax]; ret": 0x23B7A,
        },
    },
}

LIBC_GADGETS = [
    "mov rsp, [rdi + 0x38]; pop rdi; ret",
    "mov rax, [rax]; ret",
]

LIBC_OFFSETS = {
    "A YEAR OF SPRINGS": {
        "PS4": {
            "sceKernelGetModuleInfoFromAddr": 0x113908,
            "gettimeofday": 0x1139A0,
            "strcmp": 0xB0AE0,
            "__error": 0x168,
            "strerror": 0x37000,
        }
    },
    "Arcade Spirits: The New Challengers": {
        "PS4": {
            "sceKernelGetModuleInfoFromAddr": 0x113908,
            "gettimeofday": 0x1139A0,
            "strcmp": 0xB0AE0,
            "__error": 0x168,
            "strerror": 0x37000,
        },
        "PS5": {
            "sceKernelGetModuleInfoFromAddr": 0x113C08,
            "gettimeofday": 0x113B18,
            "strcmp": 0x392B0,
            "__error": 0xCC5A0,
            "strerror": 0x73520,
        },
    },
    "One Night Stand": {
        "PS4": {
            "sceKernelGetModuleInfoFromAddr": 0x203FC8,
            "gettimeofday": 0x204060,
            "strcmp": 0xB5930,
            "__error": 0x168,
            "strerror": 0x42540,
            "Thrd_create": 0x573F0,
            "Thrd_join": 0x57260,
            "Thrd_exit": 0x572E0,
            "calloc": 0x57E00,
            "memcpy": 0x4DF50,
            "setjmp": 0xB5630,
            "longjmp": 0xB5680,
            "Mtx_init": 0x57670,
            "Mtx_lock": 0x57700,
            "Mtx_unlock": 0x576F0,
        },
        "PS5": {
            "sceKernelGetModuleInfoFromAddr": 0x10FA88,
            "gettimeofday": 0x10F9A0,
            "strcmp": 0x379E0,
            "__error": 0xC7A30,
            "strerror": 0x6F610,
        },
    },
    "Blind Men": {
        "PS4": {
            "sceKernelGetModuleInfoFromAddr": 0x11B9E0,
            "gettimeofday": 0x11BA78,
            "strcmp": 0xB3060,
            "__error": 0x168,
            "strerror": 0x38340,
            "Thrd_exit": 0x4DDA0,
            "calloc": 0x4E910,
            "memcpy": 0x44150,
            "setjmp": 0xB2D60,
            "longjmp": 0xB2DB0,
            "Mtx_init": 0x4E1A0,
            "Mtx_lock": 0x4E230,
            "Mtx_unlock": 0x4E220,
        },
    },
}

EXEC_OFFSETS = {
    "A YEAR OF SPRINGS": {
        "PS4": {
            "func_repr": 0x3B6D70,
            "strcmp": 0xC5F608,
        }
    },
    "Arcade Spirits: The New Challengers": {
        "PS4": {
            "func_repr": 0x353CA0,
            "strcmp": 0xC61F28,
        },
        "PS5": {
            "func_repr": 0x4015C0,
            "strcmp": 0xB96F28,
        },
    },
    "One Night Stand": {
        "PS4": {
            "func_repr": 0x1E3440,
            "strcmp": 0xA5AFF8,
        },
        "PS5": {
            "func_repr": 0x463C90,
            "strcmp": 0xB7C280,
        },
    },
    "Blind Men": {
        "PS4": {
            "func_repr": 0x1E6530,
            "strcmp": 0xA5CF48,
        },
    },
}
