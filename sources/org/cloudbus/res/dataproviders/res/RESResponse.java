package org.cloudbus.res.dataproviders.res;

import lombok.Data;
import org.cloudbus.res.model.CloudDatacenter;
import org.cloudbus.res.model.EdgeDatacenter;

import java.util.List;

@Data
public class RESResponse {
    private String simulationDate;
    private List<EdgeDatacenter> edgeDatacenters;
    private List<CloudDatacenter> cloudDatacenters;
}