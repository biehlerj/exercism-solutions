import java.util.HashMap;
import java.util.Map;

public class DialingCodes {
    Map<Integer, String> countryCodes = new HashMap<Integer, String>();

    public Map<Integer, String> getCodes() {
        return this.countryCodes;
    }

    public void setDialingCode(Integer code, String country) {
        this.countryCodes.put(code, country);
    }

    public String getCountry(Integer code) {
        return this.countryCodes.get(code);
    }

    public void addNewDialingCode(Integer code, String country) {
        if (this.getCountry(code) == null) {
            this.countryCodes.put(code, country);
        }
    }

    public Integer findDialingCode(String country) {
        for (Map.Entry<Integer, String> countryEntry : this.countryCodes.entrySet()) {
            if (countryEntry.getValue().equals(country))
                return countryEntry.getKey();
        }
        return null;
    }

    public void updateCountryDialingCode(Integer code, String country) {
        if (this.findDialingCode(country) != null) {
            this.countryCodes.remove(code);
            this.countryCodes.put(code, country);
        }
    }
}
