public class Franc extends Money {

    Franc(int amount, String currency) {
        super(amount, currency);
    }

    /**
     * Multiply the amount by the multiplier.
     * @param multiplier Multiplier of the base amount
     * @return new Franc object with multiplied amount
     */
    public Money times(int multiplier) {
        return new Franc(this.amount * multiplier, currency);
    }
}
