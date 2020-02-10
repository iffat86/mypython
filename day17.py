import configparser


parser = configparser.ConfigParser()

parser.read("config.cfg")

print(parser.sections())
print(parser.has_section("Section 1"))

using_travel_time = bool(parser["DEFAULT"]["UseTimeTravel"])
print(using_travel_time)

opd = parser["DEFAULT"].getboolean("ObeyPrimeDirective")
print(opd)

speed = parser["DEFAULT"].getfloat("Ship Speed")
print(speed)

title = parser["Section 1"]["Title"]
print(title)


YearJump =parser["DEFAULT"].getint("DefaultYearJump")
print(YearJump)
print(type(YearJump))