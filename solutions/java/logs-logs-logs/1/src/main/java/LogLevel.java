public enum LogLevel {
    TRACE("TRC", 1),
    DEBUG("DBG", 2),
    INFO("INF", 4),
    WARNING("WRN", 5),
    ERROR("ERR", 6),
    FATAL("FTL", 42),
    UNKNOWN("UNKNOWN", 0);

    private final String logLevel;
    private final int levelNumber;

    LogLevel(String logLevel, int levelNumber) {
        this.logLevel = logLevel;
        this.levelNumber = levelNumber;
    }

    public String getLogLevel() {
        return this.logLevel;
    }

    public int getLevelNumber() {
        return this.levelNumber;
    }

    public static LogLevel fromLevel(String shortCode) {
        for (LogLevel level : LogLevel.values()) {
            if (level.logLevel.equals(shortCode))
                return level;
        }
        return UNKNOWN;
    }
}
