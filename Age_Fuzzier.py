import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import skfuzzy.membership as mf

x = np.arange(0, 80, 1)

#DEFINITIONS OF MEMBERSHIP FUNCTIONS
age_child = mf.pimf(x, -1, 0, 10, 18)
age_young = mf.pimf(x, 10, 20, 25, 40)
age_adult = mf.pimf(x, 30, 40, 50, 65)
age_elder = mf.pimf(x, 50, 65, 80, 81)

#DRAWING MEMBERSHIP FUNCTIONS
fig, (ax0) = plt.subplots(nrows = 1, figsize = (20, 10))
ax0.plot(x, age_child, 'r', linewidth = 2, label ='Child')
ax0.plot(x, age_young, 'b', linewidth = 2, label ='Young')
ax0.plot(x, age_adult, 'c', linewidth = 2, label ='Adult')
ax0.plot(x, age_elder, 'g', linewidth = 2, label ='Elder')
plt.xlabel("AGE", size = 20)
plt.ylabel("µ(x)", size = 20)
ax0.legend()

#FINDING MEMBERSHIP GRADES ACCORDING TO THE VALUES
input_age = int(input("Input Age: "))

u1 = fuzz.interp_membership(x, age_child, input_age)
u2 = fuzz.interp_membership(x, age_young, input_age)
u3 = fuzz.interp_membership(x, age_adult, input_age)
u4 = fuzz.interp_membership(x, age_elder, input_age)

ax0.vlines(input_age, 0, u1, linestyles ='--', linewidth = 1, color ='black')
ax0.hlines(u1, 0, input_age, linestyles ='--', linewidth = 1, color ='black')
if u1 != 0:
    ax0.plot(input_age, u1, 'ro', linewidth = 5)

ax0.vlines(input_age, 0, u2, linestyles ='--', linewidth = 1, color ='black')
ax0.hlines(u2, 0, input_age, linestyles ='--', linewidth = 1, color ='black')
if u2 != 0:
    ax0.plot(input_age, u2, 'ro', linewidth = 5)

ax0.vlines(input_age, 0, u3, linestyles ='--', linewidth = 1, color ='black')
ax0.hlines(u3, 0, input_age, linestyles ='--', linewidth = 1, color ='black')
if u3 != 0:
    ax0.plot(input_age, u3, 'ro', linewidth = 5)

ax0.vlines(input_age, 0, u4, linestyles ='--', linewidth = 1, color ='black')
ax0.hlines(u4, 0, input_age, linestyles ='--', linewidth = 1, color ='black')
if u4 != 0:
    ax0.plot(input_age, u4, 'ro', linewidth = 5)

u1 = round(u1, 3)
u2 = round(u2, 3)
u3 = round(u3, 3)
u4 = round(u4, 3)


print("""

               {}      {}         {}          {}
{} Age -->  -------- + -------- + -------- + --------
              Child      Young      Adult     Elder


""".format(u1, u2, u3, u4, input_age))

plt.show()