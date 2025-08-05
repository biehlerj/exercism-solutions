class Badge {
    public String print(Integer id, String name, String department) {
        String badge = null;

        if (id == null && department == null) {
            badge = String.format("%s - OWNER", name);
        } else if (id == null) {
            badge = String.format("%s - %s", name, department.toUpperCase());
        } else if (department == null) {
            badge = String.format("[%s] - %s - OWNER", id, name);
        } else {
            badge = String.format("[%s] - %s - %s", id, name, department.toUpperCase());
        }

        return badge;
    }
}
