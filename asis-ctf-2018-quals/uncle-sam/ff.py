import random
import gmpy2
import sys

sys.setrecursionlimit(10000)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def gcd(a,b):
    return egcd(a,b)[0]

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

# from Crypto.Util.number import *
pubkey=1043247381320041410146374847683905608886067988802815759655490071506964811427733496668055364700822779908166748193534341903285387332658081562041534228961538451830025041762537639985150344917584064827615356535763872539925989984117068207555498700585376330731428359489791600319636079777025344217248475485835298689437926003958578141784379857951264973109214803916445702964047899447002191548965239884095802091798787988745415178578597206815122915438351636672681355517982410123569961242563194480399347961753678159210217993526738306796503660563163029287419732210247579793266891085178817047536758465239950861266592524206390869822972469137566045176690277813352563392838847417674529251627419479815097868890993153215515488877097760272399483111013602618554846096893805108827211344467797072352072430591318485091677011261912992157762106672216780766138057271434398274272110062768324672899209610001835423246735718435995420720133657793744810610657
privkey=105717877672224295784291675385546750129601472163379527375367128238003471793097341763391999503913659542087520808364287167645349555897774428176288829031477703594776341268160433668976237198330124904372546897953955241778475322074160469767162566234358907740412805211247598698481640207956827199048419949848619731050860757808082106844953602176503247786535423423104239566910713528691298692332149783689032722772009974404716783312200885555343877611094998117307970399241640213553820043460140493803404190774171912962651075100983834071259021038322886114660028788229094872545516054757700068264628024524394995795135464746570071201
enc=343369686707916921497078851452395954252074753628024855326592148594828266567853497784448902839960599855457261387659174943864861324798607407210198762531665500523668627672623380100283047707927966101715266190355476680204081288124100983003649559499979731342450364456322062273208742008750774795951290651360492364136674198126979777860541228166734597108964573061640243513571440689299166495541329990802602494896619995591485311779060353650700199981044058309406067935205196708178000370643018639282003328307492888263256672104905274453644042024751439967243049147724769464785043328741645419214885736940487139062463786022104540986811119563549305718088453842093257734689508882969016290658885961965896726616361694426487326338043950416067501288065942862535560013037283761552797410980713186506671844418096395304234050342551849999867017770968633512178545044838766793795733222455421862835695299142219006201321417882617773291364153890050471244104
# print long_to_bytes(pow(enc,privkey,pubkey))

n=pubkey
d=privkey

f = n*(n*d-1)*(n*d-1)
g = f
while g % 2 == 0:
    g /= 2
print 'g=%d'%(g,)

def fuck():
    while True:
        a = 0
        while True:
            a = random.randint(0,n)
            b = pow(a, g, n)
            if b != 1 and b != n - 1:
                break 
        print 'a=%d'%(a,)
        while True:
            print '\tb=%d'%(b,)
            c = pow(b, 2, n)
            if c == 1:
                print 'FACTORED'
                p,q = gcd(n,b-1),gcd(n,b+1)
                q,p = min(p,q), int(gmpy2.isqrt(max(p,q)))
                return p,q
            if c == n - 1 or b == c:
                print "a didn't work"
                break
            b = c

p,q = fuck()
print 'p = %d'%(p,)
print 'q = %d'%(q,)
phi_n=p*(p-1)*(q-1)
real_d = (p-1)*(q-1)
phi=(p-1)*(p)*(q-1)
x=pow(enc, modinv((p+q-1),phi), n)
a=(x%q)
d=modinv(p,q-1)
print hex(int(pow(a,d,q)))
# ASIS{Y0u_c4N_m4n493_Schmidt_5am0A_CryP7o_SysT3M!!}