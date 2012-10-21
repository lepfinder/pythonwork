import memcache
mc = memcache.Client(['127.0.0.1:11211'],debug=1)

mc.set("a","hello")
value = mc.get("a")

mc.set("name","Bossssssssb")
mc.set("aaa","fffff")
print value
