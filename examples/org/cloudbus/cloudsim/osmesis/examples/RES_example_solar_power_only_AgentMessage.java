/*
 * Title:        IoTSim-Osmosis-RES 1.0
 * Description:  IoTSim-Osmosis-RES enables the testing and validation of osmotic computing applications
 * 			     over heterogeneous edge-cloud SDN-aware environments powered by the Renewable Energy Sources.
 *
 * Licence:      GPL - http://www.gnu.org/copyleft/gpl.html
 *
 * Copyright (c) 2021, Newcastle University (UK) and Saudi Electronic University (Saudi Arabia) and
 *                     AGH University of Science and Technology (Poland)
 *
 */

package org.cloudbus.cloudsim.osmesis.examples;

import org.cloudbus.agent.AgentMessage;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

public class RES_example_solar_power_only_AgentMessage extends AgentMessage {
    List<String> availableMELs = new ArrayList<>();
    double greenEnergyRatio;
    double lowEmissionPercentage;
    double lat;
    double lon;

    public RES_example_solar_power_only_AgentMessage() {
        //This is necessary for dynamic agent instance creation.
    }

    public double getLowEmissionPercentage() {
        return lowEmissionPercentage;
    }

    public void setLowEmissionPercentage(double lowEmissionPercentage) {
        this.lowEmissionPercentage = lowEmissionPercentage;
    }

    public double getLat() {
        return lat;
    }

    public void setLat(double lat) {
        this.lat = lat;
    }

    public double getLon() {
        return lon;
    }

    public void setLon(double lon) {
        this.lon = lon;
    }

    public double getGreenEnergyRatio() {
        return greenEnergyRatio;
    }

    public void setGreenEnergyRatio(double greenEnergyRatio) {
        this.greenEnergyRatio = greenEnergyRatio;
    }

    public List<String> getAvailableMELs() {
        return availableMELs;
    }

    public void addMEL(String mel){
        availableMELs.add(mel);
    }

    public RES_example_solar_power_only_AgentMessage(Long id, String source, Set<String> destination) {
        super(id, source, destination);
    }
}
