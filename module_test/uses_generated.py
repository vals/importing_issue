def try_import():
    try:
        import generated
    except:
        print("Could not import")
        return 0
    else:
        print("Succeeded with importing: A = {}".format(generated.A))
        return generated.A
