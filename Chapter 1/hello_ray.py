nx = 300;
ny = 200;

file = open("img.ppm", "w+");

file.write("P3\n");
file.write(str(nx));
file.write(" ");
file.write(str(ny));
file.write("\n255\n");

j = ny - 1;
while (j >= 0):
    i = 0;
    while (i < nx):
        r = float(i) / float(nx);
        g = float(j) / float(ny);
        b = 0.2;
        ir = int(255.99 * r);
        ig = int(255.99 * g);
        ib = int(255.99 * b);
        file.write(str(ir));
        file.write(" ");
        file.write(str(ig));
        file.write(" ");
        file.write(str(ib));
        file.write("\n");
        i = i + 1;
    j = j - 1;
