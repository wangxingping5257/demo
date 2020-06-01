from django.test import TestCase

# Create your tests here.


def compare_version(version1, version2):

    v1_list = version1.split(".")
    v2_list = version2.split(".")

    for index, i in enumerate(v1_list, 0):
        try:
            v2 = v2_list[index]
        except IndexError:
            return 1
        if int(i) > int(v2):
            return 1
        if int(i) < int(v2):
            return -1
    return 0

if __name__ == '__main__':
    print(compare_version("0.1", "1.1"))  # -1
    print(compare_version("1.01", "1"))  # 1
    print(compare_version("7.5.2.4", "7.5.3")) # -1
    print(compare_version("1.01", "1.001"))  # 0
    print(compare_version("1.0", "1.0.0"))  # 0


