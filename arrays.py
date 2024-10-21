datorer = ["Dator 1", "Dator 2", "Dator 3", "Dator 4", "Dator 5"]
service_datorer = []
datorer_pa_service = 0

while datorer_pa_service < 3:
    print("\nDatorer i företaget:")
    for i in range(len(datorer)):
        print(f"{i + 1}. {datorer[i]}")

    print("\nDatorer på service:")
    for i in range(len(service_datorer)):
        print(f"{i + 1}. {service_datorer[i]}")

    try:
        val = int(input("\nVälj vilken dator du vill skicka på service (ange siffra): ")) - 1
        
        if 0 <= val < len(datorer):
            dator_till_service = datorer[val]
            service_datorer.append(dator_till_service)
            datorer.pop(val)
            datorer_pa_service += 1
            print(f"\n{dator_till_service} har skickats på service.")
        else:
            print("Ogiltigt val, försök igen.")
    
    except ValueError:
        print("Ange en giltig siffra.")

print("\nTre datorer har skickats på service. Programmet avslutas.")
