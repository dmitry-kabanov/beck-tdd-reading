import org.junit.Test;

import static org.junit.Assert.*;

public class TestFranc {
    @Test
    public void testMultiplication() {
        Money five = Money.franc(5);
        assertEquals(Money.franc(10), five.times(2));
        assertEquals(Money.franc(15), five.times(3));
    }

    @Test
    public void testEquality() {
        assertEquals(Money.franc(5), new Franc(5));
        assertNotEquals(Money.franc(5), new Franc(6));
    }
}
