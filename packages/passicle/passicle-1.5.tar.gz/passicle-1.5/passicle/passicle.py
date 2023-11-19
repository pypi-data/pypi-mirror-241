def generate(service_name, key):
    list1 = ']ezdESiKJGPIX(*@m374=+Z6faRN\"2&y^9VqY8A1B`%hs.v}#L0pQD:o;C-x,!ul)bHU{wW/tF\'r~Ong?c[_MjT$k5'
    list2 = '3h*4c&P(H?dY}t=%!GXjT@{/pF1r7glOqf:SEubA5LB#vW[w)-R.V,U`zy\"e;ZN0]$6^mJ2\'sxM9k+_~a8KinICoDQ'
    password = ''
    for i in range(len(service_name)):
        c = service_name[i]
        index = list1.index(c)
        k = key[index % len(key)]
        index2 = list1.index(k)
        newIndex = (index + index2 + i) % len(list1)
        if i % 2 == 0:
            newChar = list1[newIndex]
        else:
            newChar = list2[newIndex]
        password += newChar
    password += list1[len(key)]
    password += list1[len(service_name)]
    password += list1[len(service_name) + len(key)]
    password += list1[len(password)]
    return password