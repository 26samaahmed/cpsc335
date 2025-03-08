# Greedy Algorithm
def activity_selection(activities):
  # Step 1: Sort all talks/activites by their end time
  activities.sort(key=lambda x: x[1])

  # Step 2: Initialize the selected activities list with the first activity
  selected_activities = [activities[0]] # the first activity is always selected
  last_selected = activities[0] # keepig track of the last selected activity

  # Step 3: Iterate through the remaining activities
  for i in range(1, len(activities)):
    # Step 4: Check if the start time of the current activity is after ..
    if activities[i][0] >= last_selected[1]:
      selected_activities.append(activities[i])
      last_selected = activities[i]
  return selected_activities


# Example
activities = [
  (1, 3), (2, 5), (4, 6), (7, 9), (5, 8)
]

print("Max set of non-overlapping activities: ", activity_selection(activities))