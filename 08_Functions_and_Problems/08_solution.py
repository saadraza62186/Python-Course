def inform(**kwargs):
    for key, val in kwargs.items():
        print(f"{key} : {val}")
inform(name="superman", power="fly in sky")
inform(name="superman")
inform(name="superman", power="fly in sky", enemy="batman")