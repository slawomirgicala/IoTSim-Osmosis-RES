package org.cloudbus.res.dataproviders.res;

import java.io.IOException;

public class test {
    public static void main(String[] args) throws IOException {
        RESParse pv=new RESParse();
        System.out.println(pv.parse("inputFiles/Example_RES_config.json"));
    }
}