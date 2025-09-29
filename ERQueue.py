class ERQueue:
    def __init__(self):
        self.arrivals = []
 
    def empty(self):
        return len(self.arrivals) == 0

    def arrive(self, name: str, priority: int, condition: str, time: str):
        arrival_data = {
            "Priority": priority,
            "Name": name, 
            "Condition": condition,
            "Time": time
        }
        self.arrivals.append(arrival_data)
        print(self.format_arrival(arrival_data))
    
    def treatNext(self):
        if self.empty():
            print("ER is empty!")
            return None
        treated_patient = self.arrivals.pop(0)
        print(">>> Treating patient now...")
        print("Treated:", self.format_arrival(treated_patient))
        return treated_patient

    def format_arrival(arrival):
        return f"[P{arrival['Priority']}] {arrival['Name']} - {arrival['Condition']} ({arrival['Time']})"

    def displayQueue(self):
        print("\n=== UPDATED QUEUE ===")
        for arrival in self.arrivals:
            print(self.format_arrival(arrival))
        

er = ERQueue()
er.arrive("Pedro Cruz", 1, "Head injury - NOW UNCONSCIOUS ⚠️", "23:52")
er.arrive("Carlos Mendoza", 2, "Compound fracture - leg", "23:50")
er.arrive("Lisa Wang", 2, "Severe asthma attack", "23:56")
er.arrive("Maria Santos", 3, "Deep laceration on arm", "23:48")
er.arrive("Ana Lim", 4, "Sprained ankle", "23:49")

er.displayQueue()
er.treatNext()
er.displayQueue()