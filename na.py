"""
	Creates and stores `Activity` and `SubstanceIntake` objects in YAML files to be queried by dataview in Obsidian.
	
	every `SubstanceIntake` object creation triggers a new `Activity` object creation.
"""


import os
import contextlib
import yaml
import pathlib
import datetime

from typing 	import Final, Optional
from yaml		import safe_load, safe_dump
from abc        import ABC, abstractmethod

class RecordService(ABC):
    @staticmethod
    @abstractmethod
    def from_input() -> "Record":
        pass;
    
    def as_yaml(self) -> str:
        keys, values = zip(*self.__dict__.items());
        return yaml.dump(dict(zip(keys, values)));
    
    @property
    @abstractmethod
    def filename(self) -> str:
        pass
    
    def write(self, path: str) -> None:
        filepath = os.path.join(path, self.filename)
        with open(filepath, "w") as f:
            f.write("---\n" + self.as_yaml() + "---\n");
    
    def __str__(self):
        return self.as_yaml();
    
    def __repr__(self):
        return self.as_yaml();

class Activity(RecordService):
    def __init__(self, activity: str, category: str, notes: str, time: datetime.datetime):
        self.title = activity
        self.category = category
        self.notes = notes;
        self.time = time.strftime("%Y-%m-%dT%H:%M");
    
    @staticmethod
    def from_input() -> "Activity":
        return Activity(
            activity=input("activity: ").strip(),
            category=input("category: ").strip(),
            notes=input("notes: ").strip(),
            time=handle_time(input("time: ").strip())
        );
    
    @property
    def filename(self) -> str:
        return f"act_{datetime.datetime.strptime(self.time, '%Y-%m-%dT%H:%M').strftime('%Y%m%d%H%M')}.md"


class SubstanceIntake(RecordService):
    class SubstanceIntakeType:
        #	nutritional intakes
        ALL_SUGAR = "all_sugar";
        CALCIUM = "calcium";
        CHOLESTEROL = "cholesterol";
        FAT = "fat";
        FIBER = "fiber";
        IRON = "iron";
        PROTEIN = "protein";
        SODIUM = "sodium";
        VITAMIN_A = "vitamin_a";

        #	non-nutritional intakes
        WATER = "water";
        AMBER = "amber";
        CIGARETTES = "cigarettes";
        ALCOHOL = "alcohol";


    def __init__(self, substance: str, intake: str, measure: str, time: datetime.datetime):
        self.title = substance
        self.intake = intake
        self.measure = measure
        self.time = time.strftime("%Y-%m-%dT%H:%M");
        
        #	triggers creation of a new Activity object
        act = Activity(activity=f"{self.title}, {self.intake} {self.measure}", category="ego/substance-intake", notes=f"[[substances]], [[{self.title} intake]]", time=time);
        act.write(os.path.join(os.getcwd(), "registers", "activity"));
        

    @staticmethod
    def from_input() -> "SubstanceIntake":
        return SubstanceIntake(
            substance=input("substance: ").strip(),
            intake=input("intake: ").strip(),
            measure=input("measure: ").strip(),
            time=handle_time(input("time: ").strip())
        );

    @property
    def filename(self) -> str:
        return f"sbi_{datetime.datetime.strptime(self.time, '%Y-%m-%dT%H:%M').strftime('%Y%m%d%H%M')}.md"



def handle_time(time: str | None) -> str | datetime.datetime:
    def get_time(time: str | None) -> datetime.datetime:
        if time is None or time == "":
            return datetime.datetime.now();

        #   HH:MM
        if ":" in time:
            return datetime.datetime.strptime(time, "%H:%M").replace(year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day);

        #   YYYY-MM-DDTHH:MM
        try:
            return datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M");
        except ValueError as e:
            raise ValueError(f"time data {time!r} does not match format %Y-%m-%dT%H:%M") from e

    return get_time(time);

def assert_folders(folders: list[str]):
    """ creates folders if they don't exist """
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True);



SERVICES: Final[list[str]] = [
    "activity",
    "substance_intake"
];

SERVICES_ALIASES: Final[dict[str, list[str]]] = {
    "activity": ["act", "a"],
    "substance_intake": ["sbi", "sb"]
};

def service_get() -> str:
    service = input("Select service: ");
    for service_name, aliases in SERVICES_ALIASES.items():
        if service in aliases:
            return service_name;
    
    if service in SERVICES:
        return service;
    
    print("Invalid service. Please select one of the following:")
    for service in SERVICES:
        print(service);
    return service_get();



def present_app():
    print("shards automaton v. 0.0.1");

if __name__ == '__main__':
    present_app();
    
    #	Select service
    service = service_get();
    print(f"Selected service: {service}");

    #	Default registers folders
    activity_folder, substance_intake_folder = os.path.join(os.getcwd(), "registers", "activity"), os.path.join(os.getcwd(), "registers", "substance-intake");

    #	Create folders if they don't exist
    assert_folders([activity_folder, substance_intake_folder]);

    #	Select register type
    if service == "activity":
        activity = Activity.from_input();
        activity.write(activity_folder);
    elif service == "substance_intake":
        substance_intake = SubstanceIntake.from_input();
        substance_intake.write(substance_intake_folder);

