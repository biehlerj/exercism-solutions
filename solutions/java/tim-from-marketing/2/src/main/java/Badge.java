class Badge {
    public String print(Integer id, String name, String department) {
        String badge;

        if (id == null && department == null) {
            badge = name + " - OWNER";
        } else if (id == null) {
            badge = name + " - " + department.toUpperCase();
        } else if (department == null) {
            badge = "[" + id + "] - " + name + " - OWNER";
        } else {
            badge = "[" + id + "] - " + name + " - " + department.toUpperCase();
        }

        return badge;
    }
}
