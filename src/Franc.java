public class Franc extends Money {

    private String currency;

    public Franc(int amount) {
        this.amount = amount;
        this.currency = "CHF";
    }

    /**
     * Multiply the amount by the multiplier.
     * @param multiplier Multiplier of the base amount
     * @return new Franc object with multiplied amount
     */
    public Money times(int multiplier) {
        return new Franc(this.amount * multiplier);
    }

    @Override
    String currency() {
        return currency;
    }
}
