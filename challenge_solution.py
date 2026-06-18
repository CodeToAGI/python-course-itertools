"""
CodeToAGI - Episode 35 Challenge Solution
Student × Subjects Schedule Planner using itertools
"""

from itertools import product, combinations, groupby, cycle, islice
from operator import itemgetter
from collections import defaultdict
import json

# ==================== DATA ====================
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
subjects = ["Math", "Physics", "Chemistry", "Biology", "History"]

time_slots = ["9:00 AM", "10:30 AM", "1:00 PM", "2:30 PM", "4:00 PM"]

print("=== CodeToAGI Ep 35 Challenge Solution ===\n")

# Step 1: All student-subject pairs using product
print("1. All possible student-subject pairs:")
all_pairs = list(product(students, subjects))
for pair in islice(all_pairs, 10):  # Show first 10
    print(f"   {pair}")
print(f"   ... Total pairs: {len(all_pairs)}\n")

# Step 2: Possible 2-student study groups using combinations
print("2. Possible 2-student study groups:")
study_groups = list(combinations(students, 2))
for group in study_groups[:8]:
    print(f"   {group}")
print(f"   ... Total possible pairs: {len(study_groups)}\n")

# Step 3: Group student-subject pairs by subject using groupby
print("3. Grouping assignments by subject:")

# Create enriched pairs with subject as key
enriched_pairs = [{"student": s, "subject": sub} for s, sub in all_pairs]

# Must sort first for groupby!
enriched_pairs.sort(key=itemgetter('subject'))

grouped = groupby(enriched_pairs, key=itemgetter('subject'))

subject_groups = {}
for subject, group in grouped:
    subject_groups[subject] = list(group)
    print(f"   {subject}: {len(subject_groups[subject])} students")

# Step 4: Assign round-robin time slots using cycle
print("\n4. Final Schedule with Time Slots (Round-Robin):")

# Cycle through time slots
slot_cycle = cycle(time_slots)

schedule = []
for pair in islice(all_pairs, 20):  # Bonus: limit to 20 assignments
    assignment = {
        "student": pair[0],
        "subject": pair[1],
        "time": next(slot_cycle)
    }
    schedule.append(assignment)
    print(f"   {pair[0]:8} → {pair[1]:10} @ {assignment['time']}")

# Save to JSON
with open("student_schedule.json", "w") as f:
    json.dump(schedule, f, indent=2)

print(f"\n✅ Schedule saved to 'student_schedule.json' ({len(schedule)} assignments)")

# Bonus: Group schedule by subject with time slots
print("\n5. Final Schedule Grouped by Subject:")
schedule_sorted = sorted(schedule, key=itemgetter('subject'))
for subject, group in groupby(schedule_sorted, key=itemgetter('subject')):
    print(f"\n   📚 {subject}:")
    for item in list(group)[:5]:  # Show first 5 per subject
        print(f"      • {item['student']:8} @ {item['time']}")
