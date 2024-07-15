# gpa-calculator

a python gpa calculator using the grades to points conversion (gtp) scale of an unspecified university

## future potential changes
- [x] show user's cumulative and semester gpa based on amount of semesters entered (2024.07.13)
- [x] allow for numerical input for grades instead of being limited to just letters
   - [x] automatically convert numerical grades into letters, which will automatically follow university's gtp scale
- [ ] add color to semester names when printing
- [ ] allow grades to be edited after being inputted

## existing features
* gpa calculator
* grades can be entered per semester
   * can also be viewed (via user option)
   * format `(NAME, LETTER_GRADE, POINTS, CREDIT_HOURS)`
* gpas are automatically calculated per semester and cumulatively
* numerical grade to letter grade conversion