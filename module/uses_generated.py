import sys


def try_import():
    print(sys.path)
    print("\n")
    try:
        import generated
    except:
        print("Could not import")
    else:
        print("Succeeded with importing: A = " + str(generated.A))
