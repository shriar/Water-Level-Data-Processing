# Steps for Processing Water Level Data

## Step 1: Check for Missing Date
- Verify if there are any gaps in the dates in the Excel file.
- If gaps are found, identify the missing dates.

## Step 2: Remove Repeated Dates-Times
- Remove any duplicate date and time entries from the entire Excel file.

## Step 3: Adjust Intermediate Times
- For water level data at times like 10:10, find the nearest standard time (e.g., 9:00 or 12:00).
- Replace the water level data of the nearest standard time with the data from the intermediate time (e.g., 10:10).

## Step 4: Delete Non-Standard Times
- Delete all data entries that are not at 6:00, 9:00, 12:00, 15:00, 18:00 times.
- Ensure only data at these specific times remain in the Excel file.

## Step 5: Create Missing Data
- Create missing data for 21:00, 24:00, and 3:00 times:
21:00 water level = same as 9:00 of the same day.
24:00 water level = same as 12:00 of the same day.
3:00 water level = same as 15:00 of the previous day.