def load_initial_data():
    from serv.models import Status, Type, category, subcategory
    if  Status.objects.exists():
        print("Initial data already exists, skipping creation.")
        return
    
    for name in ['Бизнес', 'Личное', 'Налог']:
        status = Status.objects.create(status_name=name)
       
    
    Type.objects.create(type_name='Пополнение')
    spis = Type.objects.create(type_name='Списание')   
    
    infra = category.objects.create(category_name = 'Инфраструктура', type = spis)
    marketing = category.objects.create(category_name = 'Маркетинг', type = spis)

    for name in ['VPS', 'Proxy']:
        subcategory.objects.create(subcategory_name=name, category=infra)

    for name in ['Farpost', 'Avito']:
        subcategory.objects.create(subcategory_name=name, category=marketing)
    
    print("Initial data loaded successfully.")