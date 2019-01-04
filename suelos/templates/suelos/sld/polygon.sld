<?xml version="1.0" encoding="ISO-8859-1"?>
<StyledLayerDescriptor version="1.0.0"
                       xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd"
                       xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc"
                       xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

    <NamedLayer>
        <Name>{{ self.campo }}</Name>
        <UserStyle>
            <Title>{{ self.campo }}</Title>
            <FeatureTypeStyle>
                {% for campo in self.camposet %}

                    <Rule>
                        <Title>{{ campo }}</Title>
                        <ogc:Filter>
                            <ogc:PropertyIsEqualTo>
                                <ogc:PropertyName>{{ self.campo }}</ogc:PropertyName>
                                <ogc:Literal>{{ campo }}</ogc:Literal>
                            </ogc:PropertyIsEqualTo>
                        </ogc:Filter>
                        <PolygonSymbolizer>

                            <Fill>
                                <CssParameter name="fill">{{ self.colors.pop }}</CssParameter>
                                <CssParameter name="fill-opacity">0.6</CssParameter>
                            </Fill>
                            <Stroke>
                                <CssParameter name="stroke">#000000</CssParameter>
                                <CssParameter name="stroke-width">0.5</CssParameter>
                                <CssParameter name="stroke-opacity">0.7</CssParameter>
                            </Stroke>

                        </PolygonSymbolizer>

                    </Rule>
                {% endfor %}

            </FeatureTypeStyle>
        </UserStyle>
    </NamedLayer>
</StyledLayerDescriptor>
