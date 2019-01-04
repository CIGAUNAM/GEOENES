<?xml version="1.0" encoding="ISO-8859-1"?>
<StyledLayerDescriptor version="1.0.0"
                       xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd"
                       xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc"
                       xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

    <NamedLayer>
        <Name>ENES:suelos_suelo</Name>
        <UserStyle>
            <Title>clase_roca</Title>
            <FeatureTypeStyle>


                <Rule>
                    <Title>Ígnea extrusiva</Title>
                    <ogc:Filter>
                        <ogc:PropertyIsEqualTo>
                            <ogc:PropertyName>clase_roca</ogc:PropertyName>
                            <ogc:Literal>Ígnea extrusiva</ogc:Literal>
                        </ogc:PropertyIsEqualTo>
                    </ogc:Filter>
                    <PolygonSymbolizer>

                        <Fill>
                            <CssParameter name="fill">#c4e6c3</CssParameter>
                            <CssParameter name="fill-opacity">0.6</CssParameter>
                        </Fill>
                        <Stroke>
                            <CssParameter name="stroke">#000000</CssParameter>
                            <CssParameter name="stroke-width">0.5</CssParameter>
                            <CssParameter name="stroke-opacity">0.7</CssParameter>
                        </Stroke>

                    </PolygonSymbolizer>

                </Rule>


                <Rule>
                    <Title>Ígnea intrusiva</Title>
                    <ogc:Filter>
                        <ogc:PropertyIsEqualTo>
                            <ogc:PropertyName>clase_roca</ogc:PropertyName>
                            <ogc:Literal>Ígnea intrusiva</ogc:Literal>
                        </ogc:PropertyIsEqualTo>
                    </ogc:Filter>
                    <PolygonSymbolizer>

                        <Fill>
                            <CssParameter name="fill">#8ecea0</CssParameter>
                            <CssParameter name="fill-opacity">0.6</CssParameter>
                        </Fill>
                        <Stroke>
                            <CssParameter name="stroke">#000000</CssParameter>
                            <CssParameter name="stroke-width">0.5</CssParameter>
                            <CssParameter name="stroke-opacity">0.7</CssParameter>
                        </Stroke>

                    </PolygonSymbolizer>

                </Rule>


                <Rule>
                    <Title>Metamórfica</Title>
                    <ogc:Filter>
                        <ogc:PropertyIsEqualTo>
                            <ogc:PropertyName>clase_roca</ogc:PropertyName>
                            <ogc:Literal>Metamórfica</ogc:Literal>
                        </ogc:PropertyIsEqualTo>
                    </ogc:Filter>
                    <PolygonSymbolizer>

                        <Fill>
                            <CssParameter name="fill">#60b28b</CssParameter>
                            <CssParameter name="fill-opacity">0.6</CssParameter>
                        </Fill>
                        <Stroke>
                            <CssParameter name="stroke">#000000</CssParameter>
                            <CssParameter name="stroke-width">0.5</CssParameter>
                            <CssParameter name="stroke-opacity">0.7</CssParameter>
                        </Stroke>

                    </PolygonSymbolizer>

                </Rule>


                <Rule>
                    <Title>N/A</Title>
                    <ogc:Filter>
                        <ogc:PropertyIsEqualTo>
                            <ogc:PropertyName>clase_roca</ogc:PropertyName>
                            <ogc:Literal>N/A</ogc:Literal>
                        </ogc:PropertyIsEqualTo>
                    </ogc:Filter>
                    <PolygonSymbolizer>

                        <Fill>
                            <CssParameter name="fill">#3f927e</CssParameter>
                            <CssParameter name="fill-opacity">0.6</CssParameter>
                        </Fill>
                        <Stroke>
                            <CssParameter name="stroke">#000000</CssParameter>
                            <CssParameter name="stroke-width">0.5</CssParameter>
                            <CssParameter name="stroke-opacity">0.7</CssParameter>
                        </Stroke>

                    </PolygonSymbolizer>

                </Rule>


                <Rule>
                    <Title>Sedimentaria</Title>
                    <ogc:Filter>
                        <ogc:PropertyIsEqualTo>
                            <ogc:PropertyName>clase_roca</ogc:PropertyName>
                            <ogc:Literal>Sedimentaria</ogc:Literal>
                        </ogc:PropertyIsEqualTo>
                    </ogc:Filter>
                    <PolygonSymbolizer>

                        <Fill>
                            <CssParameter name="fill">#297170</CssParameter>
                            <CssParameter name="fill-opacity">0.6</CssParameter>
                        </Fill>
                        <Stroke>
                            <CssParameter name="stroke">#000000</CssParameter>
                            <CssParameter name="stroke-width">0.5</CssParameter>
                            <CssParameter name="stroke-opacity">0.7</CssParameter>
                        </Stroke>

                    </PolygonSymbolizer>

                </Rule>


                <Rule>
                    <Title>Volcanosedimentaria</Title>
                    <ogc:Filter>
                        <ogc:PropertyIsEqualTo>
                            <ogc:PropertyName>clase_roca</ogc:PropertyName>
                            <ogc:Literal>Volcanosedimentaria</ogc:Literal>
                        </ogc:PropertyIsEqualTo>
                    </ogc:Filter>
                    <PolygonSymbolizer>

                        <Fill>
                            <CssParameter name="fill">#1d4f60</CssParameter>
                            <CssParameter name="fill-opacity">0.6</CssParameter>
                        </Fill>
                        <Stroke>
                            <CssParameter name="stroke">#000000</CssParameter>
                            <CssParameter name="stroke-width">0.5</CssParameter>
                            <CssParameter name="stroke-opacity">0.7</CssParameter>
                        </Stroke>

                    </PolygonSymbolizer>

                </Rule>


            </FeatureTypeStyle>
        </UserStyle>
    </NamedLayer>
</StyledLayerDescriptor>
