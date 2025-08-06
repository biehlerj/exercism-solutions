class Fighter {

    boolean isVulnerable() {
        return true;
    }

    int getDamagePoints(Fighter fighter) {
        return 1;
    }
}

class Warrior extends Fighter {

    @Override
    public String toString() {
        return "Fighter is a Warrior";
    }

    @Override
    boolean isVulnerable() {
        return false;
    }

    @Override
    int getDamagePoints(Fighter fighter) {
        return fighter.isVulnerable() ? 10 : 6;
    }
}

class Wizard extends Fighter {
    boolean isSpellPrepared = false;

    @Override
    public String toString() {
        return "Fighter is a Wizard";
    }

    public void prepareSpell() {
        this.isSpellPrepared = true;
    }

    @Override
    boolean isVulnerable() {
        return isSpellPrepared ? false : true;
    }

    @Override
    int getDamagePoints(Fighter fighter) {
        return isSpellPrepared ? 12 : 3;
    }
}
