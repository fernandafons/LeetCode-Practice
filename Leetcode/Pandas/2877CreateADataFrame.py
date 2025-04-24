# 2877. Create a DataFrame from List
"""
Write a solution to create a DataFrame from a 2D list called student_data. 
This 2D list contains the IDs and ages of some students.
The DataFrame should have two columns, student_id and age, and be in the same 
order as the original 2D list.

The result format is in the following example.

Example 1:

Input:
student_data:
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
Explanation:
A DataFrame was created on top of student_data, with two columns named student_id and age.
"""

#SOLUTION

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

#EXPLANATION
"""
1. Importing Pandas
    import pandas as pd
    Pandas is a powerful Python library for data manipulation and analysis.
    We import it with the alias pd for convenience (a common convention in the data science community).

2. Function Definition
    def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    This defines a function named createDataframe that takes one argument:
    student_data: A 2D list (List[List[int]]) where each inner list contains a student's [ID, age].
    The -> pd.DataFrame part is a type hint, indicating that the function returns a Pandas DataFrame.

3. Creating the DataFrame
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    pd.DataFrame() is the Pandas function used to create a DataFrame (a table-like structure).
    Parameters:
        student_data: The input 2D list (e.g., [[1, 15], [2, 11], ...]).
        columns=['student_id', 'age']: Assigns column names to the DataFrame.

4. Returning the Result
    return df
    The function returns the constructed DataFrame, which is the expected output.
    Using print(df) would display the DataFrame but not return it, causing errors in automated testing.
    return is essential for the function to work correctly in programming challenges.
"""