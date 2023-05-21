from enum import Enum


class RegEx(Enum):
    CARD_NUMBER = (
        r'\d{16}',
        [
            'credit card number must have 16 symbols'
        ]
    )
    PROFANITY_FILTER = (
        r'^(((a[sz5]*)|(b[ou0]t+))((h[o0]+[l1!]e[sz5]*)|(w[i1!]pe[sz5]*)|(face)))|(ba[sz5]+t[ae*]rd[sz5]*)|(b[i1!]+a?tch[es]*)|(b((re?a[sz5]t[\w]*)|(o+b))[sz5]?)|(c[o0]+c?k[sz5]*.((s[ou0]c?ker)|(h[ae*]ad))?)|(c(([l1!]+[i1!]+t([o0]r[i1!])?)|(unt)|(awk))[sz5]*)|(dil+d[o0][sz5]*)|(d[i1!]c[ck]y?)|([\w015!]*fuc?k+([er]+|[ahn]+|[ing]+|)[sz5]*\w*)|(fai?g+[io01!]*t?[sz5]*)|(m[au][sz5]te?rba?i?t[ersz5]*)|(p[ae]n[i1!][sz5])|(\w*sex+y?)|(t[i1!]+t+[i1!]+e[sz5]?)|(x{3,}|jerk|whoe)$',
        [
            'the "brand" field cannot contain obscene words'
        ]
    )
    MODEL_PROFANITY_FILTER = (
        r'^(((a[sz5]*)|(b[ou0]t+))((h[o0]+[l1!]e[sz5]*)|(w[i1!]pe[sz5]*)|(face)))|(ba[sz5]+t[ae*]rd[sz5]*)|(b[i1!]+a?tch[es]*)|(b((re?a[sz5]t[\w]*)|(o+b))[sz5]?)|(c[o0]+c?k[sz5]*.((s[ou0]c?ker)|(h[ae*]ad))?)|(c(([l1!]+[i1!]+t([o0]r[i1!])?)|(unt)|(awk))[sz5]*)|(dil+d[o0][sz5]*)|(d[i1!]c[ck]y?)|([\w015!]*fuc?k+([er]+|[ahn]+|[ing]+|)[sz5]*\w*)|(fai?g+[io01!]*t?[sz5]*)|(m[au][sz5]te?rba?i?t[ersz5]*)|(p[ae]n[i1!][sz5])|(\w*sex+y?)|(t[i1!]+t+[i1!]+e[sz5]?)|(x{3,}|jerk|whoe)$',
        [
            'the "model" field cannot contain obscene words'
        ])
    CITY_PROFANITY_FILTER = (
        r'^(((a[sz5]*)|(b[ou0]t+))((h[o0]+[l1!]e[sz5]*)|(w[i1!]pe[sz5]*)|(face)))|(ba[sz5]+t[ae*]rd[sz5]*)|(b[i1!]+a?tch[es]*)|(b((re?a[sz5]t[\w]*)|(o+b))[sz5]?)|(c[o0]+c?k[sz5]*.((s[ou0]c?ker)|(h[ae*]ad))?)|(c(([l1!]+[i1!]+t([o0]r[i1!])?)|(unt)|(awk))[sz5]*)|(dil+d[o0][sz5]*)|(d[i1!]c[ck]y?)|([\w015!]*fuc?k+([er]+|[ahn]+|[ing]+|)[sz5]*\w*)|(fai?g+[io01!]*t?[sz5]*)|(m[au][sz5]te?rba?i?t[ersz5]*)|(p[ae]n[i1!][sz5])|(\w*sex+y?)|(t[i1!]+t+[i1!]+e[sz5]?)|(x{3,}|jerk|whoe)$',
        [
            'the "city_of_sale" field cannot contain obscene words'
        ])

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
