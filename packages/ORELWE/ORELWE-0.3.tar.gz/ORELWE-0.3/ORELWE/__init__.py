from .main import modMatInv
from .main import modInv
from .main import minor
from .main import dot_mod
from .main import Hash_1
from .main import Hash_23
from .main import key_gen
from .main import convert_message
from .main import convert_token
from .main import ore_test

K1, IK1, K2, IK2, mod = key_gen()
Message = convert_message()
H1 = Hash_1(Message,IK2, K1,mod)
tk1, tk2 = convert_token()
H2, H3 = Hash_23(tk1,tk2,IK1,K2,mod)
ore_test(mod)


