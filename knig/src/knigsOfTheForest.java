import java.util.PriorityQueue;

public class knigsOfTheForest {
    public static void main(String[] args)
    {
        int k = 2;
        int n = 4;

        PriorityQueue<Pair> pq = new PriorityQueue<>();

        Pair obj1 = new Pair(2013, 2);
        Pair obj2 = new Pair(2011, 1);
        Pair obj3 = new Pair(2011, 3);
        Pair obj4 = new Pair(2014, 4);
        Pair obj5 = new Pair(2012, 6);

        Pair karl = new Pair(2013, 2);

        pq.add(obj1);
        pq.add(obj2);
        pq.add(obj3);
        pq.add(obj4);
        pq.add(obj5);

        while(!pq.isEmpty())
        {
            Pair strongest = pq.poll();

            if (strongest.getYear() == karl.getYear() && strongest.getStrength() == karl.getStrength())
            {
                System.out.println(karl.getYear());
                return;
            }
        }

        System.out.println("unknown");


    }
    public static class Pair implements Comparable<Pair>
    {
        int year, strength;

        public Pair(int year, int strength)
        {
            this.year = year;
            this.strength = strength;
        }

        public int compareTo(Pair o)
        {
            int yearComparison = Integer.compare(this.year, o.year);

            if (yearComparison != 0)
            {
                return yearComparison;
            }
            else
            {
                return Integer.compare(o.strength, this.strength);
            }
        }
        
        public int getYear()
        {
            return this.year;
        }

        public int getStrength()
        {
            return this.strength;
        }
    }


}