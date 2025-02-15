from dataclasses import dataclass


@dataclass
class Color:
    h: int = 0
    s: int = 0
    v: int = 0
    
    def to_hex(self):
        if self.h is None:
            return f'#{(self.v * 255) // 100:02x}{(self.v * 255) // 100:02x}{(self.v * 255) // 100:02x}'
        i = (self.h // 60) % 6

        v_min = ((100 - self.s) * self.v) // 100

        a = ((self.v - v_min) * self.h % 60) // 60

        v_inc = v_min + a
        v_dec = self.v - a

        match i:
            case 0:
                r, g, b = self.v, v_inc, v_min
            case 1:
                r, g, b = v_dec, self.v, v_min
            case 2:
                r, g, b = v_min, self.v, v_inc
            case 3:
                r, g, b = v_min, v_dec, self.v
            case 4:
                r, g, b = v_inc, v_min, self.v
            case 5:
                r, g, b = self.v, v_min, v_dec

        return f'#{(r * 255) // 100:02x}{(g * 255) // 100:02x}{(b * 255) // 100:02x}'
    
    @staticmethod
    def from_hex(hex_str: str): 
        hex_str = hex_str.removeprefix('#')
        r = int(hex_str[0:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:6], 16)

        mx = max(r, g, b)
        mn = min(r, g, b)

        h: int
        if mx != mn:
            if mx == r:
                h = (60 * (g - b)) // (mx - mn)
            elif mx == g:
                h = (60 * (b - r)) // (mx - mn)
            else:
                h = (60 * (r - g)) // (mx - mn)
            h %= 360
        else: 
            h = None

        s = 0 if mx == 0 else (100 - (mn * 100 // mx))

        v = (mx * 100) // 255

        return Color(h, s, v)
    
    def with_h(self, h):
        return Color(h, self.s, self.v)
    
    def with_s(self, s):
        return Color(self.h, s, self.v)
    
    def with_v(self, v):
        return Color(self.h, self.s, v)
        
    def __str__(self):
        return self.to_hex()
