#Advance calculator with the basic calculations and area and volume of 2D and 3D shapes

ask = 0

while ask == 0:
    choose = int(input('''Either select a shape to calculate its area and perimeter or 
       select for basic calculations:
       1. Square
       2. Rectangle
       3. Circle
       4. Cube
       5. Cuboid
       6. Sphere
       7. Cone 
       8. Cylinder

       9. Add
       10. Subtract
       11. Multiply
       12. Divide
       ==> '''))


    # --Functions of all the shapes and figures--
    # Area, perimeter for square
    def areasq(sidesq):
        areasq = sidesq * sidesq
        return areasq


    def perisq(sidesq):
        perisq = 4 * sidesq
        return perisq


    # Area and perimeter for rectangle
    def arearect(lengthrect, widthrect):
        arearect = lengthrect * widthrect
        return arearect


    def perirect(lengthrect, widthrect):
        perirect = 2 * (lengthrect + widthrect)
        return perirect


    # Area and circumfrence for circle
    def areacir(radiuscir):
        areacir = 3.14 * (radiuscir * radiuscir)
        return areacir


    def pericir(radiuscir):
        pericir = 2 * 3.14 * radiuscir
        return pericir


    # TSA and volume for cube
    def areacube(sidecube):
        areacube = 6 * (sidecube * sidecube)
        return areacube


    def volcube(sidecube):
        volcube = sidecube * sidecube * sidecube
        return volcube


    # TSA and volume of cuboid
    def areacubo(lengthcubo, widthcubo, heightcubo):
        areacubo = (2 * lengthcubo * widthcubo) + (2 * widthcubo * heightcubo) + (2 * lengthcubo * heightcubo)
        return areacubo


    def volcubo(lengthcubo, widthcubo, heightcubo):
        volcubo = lengthcubo * widthcubo * heightcubo
        return volcubo


    # TSA and volume of a sphere
    def areasph(radiussph):
        areasph = 4 * 3.14 * radiussph * 2
        return areasph


    def volsph(radiussph):
        volsph = (4 / 3) * 3.14 * (radiussph * radiussph * radiussph)
        return volsph


    # TSA and volume of a cone
    def areacone(lengthcone, radiuscone):
        areacone = 3.14 * radiuscone * (lengthcone + radiuscone)
        return areacone


    def volcone(heightcone, radiuscone):
        volcone = (3.14 * radiuscone * radiuscone) * (heightcone / 3)
        return volcone


    # TSA and volume of cylinder
    def areacyl(heightcyl, radiuscyl):
        areacyl = 2 * 3.14 * radiuscyl * (heightcyl + radiuscyl)
        return areacyl


    def volcyl(heightcyl, radiuscyl):
        volcyl = 3.14 * heightcyl * (radiuscyl * radiuscyl)
        return volcyl


    # ----Basic Calculations----
    def sum(inp1, inp2):
        sum = inp1 + inp2
        return sum


    def sub(inp1, inp2):
        sub = inp1 - inp2
        return sub


    def mul(inp1, inp2):
        mul = inp1 * inp2
        return mul


    def div(inp1, inp2):
        div = inp1 / inp2
        return div


    # ------------------------------------------

    # Main Program starts here
    if choose == 1:
        sidesq = float(input("\nWhat is the side of your square: "))

        opt1 = int(input("\nDo you wish to calculate the Area(1) or the Perimeter of the square(2): "))
        if opt1 == 1:
            print("\nThe area of your square is: ", areasq(sidesq))

        elif opt1 == 2:
            print("\nThe perimeter of your square is: ", perisq(sidesq))
        else:
            print("Invalid Input!!")

    elif choose == 2:
        lengthrect = float(input("\nWhat is the length of your rectangle: "))
        widthrect = float(input("\nWhat is the width of your rectangle: "))

        opt2 = int(input("\nDo you wish to calculate the Area(1) or the Perimeter of the rectangle(2): "))

        if opt2 == 1:
            print("\nThe area of your rectangle is: ", arearect(lengthrect, widthrect))

        elif opt2 == 2:
            print("\nThe perimeter of your rectangle is: ", perirect)
        else:
            print("Invalid Input!!")

    elif choose == 3:
        radiuscir = float(input("\nWhat is the radius of your circle; "))

        opt3 = int(input("\nDo you wish to calculate the Area(1) or the circumfrence of the circle(2): "))

        if opt3 == 1:
            print("\nThe area of your circle is: ", areacir(radiuscir))

        elif opt3 == 2:
            print("\nThe perimeter of your circle is: ", pericir(radiuscir))
        else:
            print("Invalid Input!!")

    elif choose == 4:
        sidecube = float(input("\nWhat is the side of your cube: "))

        opt4 = int(input("\nDo you wish to calculate the Total Surface Area(1) or the volume of the cube(2): "))

        if opt4 == 1:
            print("\nThe total surface area of the cube is: ", areacube(sidecube))

        elif opt4 == 2:
            print("\nThe volume of the cube is: ", volcube(sidecube))
        else:
            print("Invalid Input!!")

    elif choose == 5:
        lengthcubo = float(input("\nWhat is the length of your cuboid: "))
        widthcubo = float(input("\nWhat is the width of your cuboid: "))
        heightcubo = float(input("\nWhat is the height of your cuboid: "))

        opt5 = int(input("\nDo you wish to calculate the Total Surface Area(1) or the volume of the cuboid(2):  "))

        if opt5 == 1:
            print("\nThe total surface of the cuboid is: ", areacubo(lengthcubo, widthcubo, heightcubo))

        elif opt5 == 2:
            print("\nThe volume of the cuboid is: ", volcubo(lengthcubo, widthcubo, heightcubo))
        else:
            print("Invalid Input!!")

    elif choose == 6:
        radiussph = float(input("\nWhat is the radius of your sphere: "))

        opt6 = int(input("\nDo you wish to calculate the Total surface area(1) or the volume of the sphere(2):  "))

        if opt6 == 1:
            print("\nThe area of your sphere is: ", areasph(radiussph))

        elif opt6 == 2:
            print("\nThe volume of the sphere is; ", volsph(radiussph))
        else:
            print("Invalid Input!!")

    elif choose == 7:
        lengthcone = float(input("\nWhat is the length of your cone: "))
        radiuscone = float(input("\nWhat is the radius of your cone: "))

        opt7 = int(input("\nDo you wish to calculate the Total Surface Area(1) or the volume of the cone(2): "))

        if opt7 == 1:
            print("\nThe area of the cone is: ", areacone(lengthcone, radiuscone))

        elif opt7 == 2:
            print("\nThe volume of the cone is: ", volcone(lengthcone, radiuscone))
        else:
            print("Invalid Input!!")

    elif choose == 8:
        heightcyl = float(input("\nWhat is the height of your cone: "))
        radiuscyl = float(input("\nWhat is the radius of your cone: "))

        opt8 = int(input("\nDo you wish to calculate the Total Surface Area(1) or the volume of the cone(2): "))

        if opt8 == 1:
            print("\nThe area of the cone is: ", areacyl(heightcyl, radiuscyl))

        elif opt8 == 2:
            print("\nThe volume of the cone is: ", volcyl(heightcyl, radiuscyl))
        else:
            print("Invalid Input!!")

    elif choose == 9:
        inp1 = int(input("Enter the first number: "))
        inp2 = int(input("Enter the second number: "))
        print("The sum of the numbers is: ", sum(inp1, inp2))

    elif choose == 10:
        inp1 = int(input("Enter the first number: "))
        inp2 = int(input("Enter the second number: "))
        print("The difference of the numbers is: ", sub(inp1, inp2))

    elif choose == 11:
        inp1 = int(input("Enter the first number: "))
        inp2 = int(input("Enter the second number: "))
        print("The sum of the numbers is: ", mul(inp1, inp2))

    elif choose == 12:
        inp1 = int(input("Enter the first number: "))
        inp2 = int(input("Enter the second number: "))
        print("The sum of the numbers is: ", div(inp1, inp2))

    else:
        print("Invalid Input!!")

    ask = int(input("Would you like to continue(0, Yes), (1, No): "))

    if ask == 1:
        break
