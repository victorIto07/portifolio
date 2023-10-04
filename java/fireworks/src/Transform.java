public class Transform {
    public double transform(double l1, double l2, double r1, double r2, double v) {
        double l_off = l2 - l1;
        double r_off = r2 - r1;
        double p = v / l_off;
        return r1 + r_off * p;
    }
}
