def try_import():
    try:
        import generated
    except:
        print("Could not import")
    else:
        print("Succeeded with importing: A = " + str(generated.A))
