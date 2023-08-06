(OOPwaiywaiy) library for exampl python OOP by Suppanimit meemungkit
====================================================================

This programing is only example for python OOP learning

วิธีติดตั้ง เปิด CMD / Terminal

::

    pip install oopwaiywaiy

วิธีใช้ [STEP 1]

เปิด IDLE ขึ้นมาแล้วพิมพ์...

::

    from oopwaiywaiy.pythonOOP import Student,Tesla,SpecialStudent,Teacher
    #Day0
    print('---- Day0 ----')
    allstudent = []
    teacher1 = Teacher(fullname='Ada lovelace')
    teacher2 = Teacher(fullname='Bill Gates')
    print(teacher1.students)



    #Day 1
    print('---- Day1 ----')
    st1 = Student('Albert','Einstein')
    allstudent.append(st1)
    teacher2.AddStudent(st1)
    print(st1.fullname)


    #Day2
    print('---- Day2 ----')
    st2 = Student('Steve','jobs')
    allstudent.append(st2)
    teacher2.AddStudent(st2)
    print(st2.fullname)

    #Day3
    print('---- Day3 ----')
    for i in range(3):
        st1.Coding()
    st2.Coding()
    st1.ShowExp()
    st2.ShowExp()

    #Day4
    print('---- Day4 ----')
    stp1 = SpecialStudent('Thomas','Edison','Hitler')
    allstudent.append(stp1)
    teacher1.AddStudent(stp1)
    print(stp1.fullname)
    print('May i give special 20 point?')
    stp1.exp = 20
    stp1.Coding()
    stp1.ShowExp()

    #Day5
    print('---- Day5 ----')
    print('How student back home with...')
    print(allstudent)

    for st in allstudent:
        print(' {} : Back home with {} '.format(st.name,st.vehicle))
        if isinstance(st,SpecialStudent):
            st.vehicle.SelfDriving(st)

    #Day6
    print('---- Day6 ----')

    teacher1.CheckStudent()
    teacher2.CheckStudent()

    print('Total point 2 student ',st1+st2)

