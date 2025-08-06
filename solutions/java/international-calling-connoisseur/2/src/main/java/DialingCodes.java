import java.util.HashMap;
import java.util.Map;

public class DialingCodes {
    Map<Integer, String> countryCodes = new HashMap<Integer, String>();

    public Map<Integer, String> getCodes() {
        return countryCodes;
    }

    public void setDialingCode(Integer code, String country) {
        countryCodes.put(code, country);
    }

    public String getCountry(Integer code) {
        return countryCodes.get(code);
    }

    public void addNewDialingCode(Integer code, String country) {
        if (!countryCodes.containsKey(code) && !countryCodes.containsValue(country)) {
            setDialingCode(code, country);
        }
    }

    public Integer findDialingCode(String country) {
        for (Map.Entry<Integer, String> countryEntry : countryCodes.entrySet()) {
            if (countryEntry.getValue().equals(country)) {
                return countryEntry.getKey();
            }
        }
        return null;
    }

    public void updateCountryDialingCode(Integer code, String country) {
        Integer oldCountryCode = findDialingCode(country);

        if (oldCountryCode != null) {
            countryCodes.remove(oldCountryCode);
            setDialingCode(code, country);
        }
    }
}
