$(function () {
    $("#main").css('height', $(window).height())
    $(window).on("resize", function () {
        $("#main").css('height', $(window).height())
    });

    var bounds = [
        [13.0, -82.0], // Southwest coordinates
        [35.0, -120.0]  // Northeast coordinates
    ];

    var map = L.map('main', {
        minZoom: 5,
        maxZoom: 22,
        maxBounds: bounds,
        zoomControl: false,
        attributionControl: false
    });
    var hash = new L.Hash(map);

    if (!window.location.hash) {
        map.setView(new L.LatLng(20.59698, -103.59609), 5);
    } else {
        myhash = window.location.hash.replace("#", "");
        myhash = myhash.split("/");
        map.setView(new L.LatLng(myhash[1], myhash[2]), myhash[0]);
    }

    satelite = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
        //attribution: '(Vista satelital Google) PAUGZM &copy; <a href="http://www.ciga.unam.mx" target=_blank>CIGA UNAM</a>.',
        maxZoom: 22,
        keepBuffer: 1,
        subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
    });

    calles = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
        //attribution: '(Vista de calles Google) PAUGZM &copy; <a href="http://www.ciga.unam.mx" target=_blank>CIGA UNAM</a>.',
        maxZoom: 22,
        keepBuffer: 1,
        subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
    });

    minimap = new L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
        minZoom: 6,
        maxZoom: 17,
        keepBuffer: 1,
        subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
    });

    satelite.addTo(map);

    $("#tabs").tabs();


    function makeLayerWMS() {
        newlayer = L.tileLayer.betterWms('http://localhost:8080/geoserver/ENES/ows?', {
            layers: 'ENES:suelos_suelo',
            tiled: true,
            format: 'image/png',
            transparent: true,
            minZoom: 5,
            maxZoom: 22,
        });
        return newlayer;
    }


    var baseLayers = {
        "Satelite (Google)": satelite,
        "Calles (Google)": calles
    };

    var overlays = {};

    L.control.custom({
        position: 'topright',
        content:
            '<button type="button" class="ui-button ui-widget ui-corner-all" data-toggle="modal" id="agregarcapa">' +
            'Agrear capa nueva' +
            '</button>',
        classes: 'btn-group-horizontal btn-group-sm',
        style: {margin: '10px', padding: '0px 0 0 0', cursor: 'pointer'},
        datas: {'foo': 'bar',},

    }).addTo(map);

    tips = $(".validateTips");

    function filtro() {
        cql = "";
        entidades = $("#id_entidad").val();
        municipios = $("#id_municipio").val();
        clases_roca = $("#id_clase_roca").val();
        tipos_roca = $("#id_tipo_roca").val();
        tipos_suelo = $("#id_tipo_suelo").val();
        usos_suelo = $("#id_uso_suelo").val();

        if (entidades.length > 0) {
            esp = "AND entidad IN ('";
            esp += entidades.join("', '");
            esp += "') ";
            cql += esp;
        }

        if (municipios.length > 0) {
            mun = "AND municipio IN ('";
            mun += municipios.join("', '");
            mun += "') ";
            cql += mun;
        }

        if (clases_roca.length > 0) {
            croca = "AND clase_roca IN ('";
            croca += clases_roca.join("', '");
            croca += "') ";
            cql += croca;
        }

        if (tipos_roca.length > 0) {
            troca = "AND tipo_roca IN ('";
            troca += tipos_roca.join("', '");
            troca += "') ";
            cql += troca;
        }

        if (tipos_suelo.length > 0) {
            tsuelo = "AND tipo_suelo IN ('";
            tsuelo += tipos_suelo.join("', '");
            tsuelo += "') ";
            cql += tsuelo;
        }

        if (usos_suelo.length > 0) {
            usuelo = "AND uso_suelo IN ('";
            usuelo += usos_suelo.join("', '");
            usuelo += "') ";
            cql += usuelo;
        }

        scql = cql.substr(0, 4);

        if (scql == 'AND ') {
            cql = cql.substr(4)
        }

        return cql;

    }

    var fcql = filtro()


    $("#ui-id-3").on("click", function () {
        fcql = filtro()
        console.log(fcql)
        $("#newtextadvanced").val(fcql)

    });

    $("#ui-id-1").on("click", function () {
        fcql = filtro()
        console.log(fcql)
        $("#newtextadvanced").val(fcql)
    });


    function checkLength(o, n, min, max) {
        if (o.val().length > max || o.val().length < min) {
            o.addClass("ui-state-error");
            updateTips("La longitud de " + n + " debe estar entre " +
                min + " y " + max + " caracteres.");
            return false;
        } else {
            return true;
        }
    }

    function updateTips(t) {
        tips
            .text(t)
            .addClass("ui-state-highlight");
        setTimeout(function () {
            tips.removeClass("ui-state-highlight", 1500);
        }, 500);
    }


    function agregarCapa() {
        var valid = true;
        console.log($("#nombre").val())
        valid = valid && checkLength($("#nombre"), "nombre", 3, 36);

        if (valid) {
            console.log("valid");
            console.log($("#nombre").val())
            overlays[$("#nombre").val()] = L.tileLayer.betterWms('http://localhost:8080/geoserver/ENES/ows?', {
                layers: 'ENES:suelos_suelo',
                tiled: true,
                format: 'image/png',
                transparent: true,
                minZoom: 5,
                maxZoom: 22,
            });

            cql = filtro()
            var fcql = $("#newtextadvanced").val()

            console.log("fcql")
            console.log(fcql)


            if (fcql != "") {
                console.log(fcql)
                cql = fcql
            }


            if (cql != "") {
                overlays[$("#nombre").val()].setParams({cql_filter: cql});
            }

            var estilo = null
            if ($("#id_colormap").val() > 0 && $("#id_campo").val() != "") {
                console.log($("#id_colormap").val())
                console.log($("#id_campo").val())
                estilo = 'http://127.0.0.1:8000/suelos/styles/polygon.sld?colormap=' + $("#id_colormap").val().toString() + '&campo=' + $("#id_campo").val();
            }

            if (estilo != null) {
                overlays[$("#nombre").val()].setParams({SLD: estilo})
            }

            overlays[$("#nombre").val()].addTo(map)

            controles.remove(map)
            controles = L.control.layers(baseLayers, overlays);

            controles.addTo(map);


            console.log(overlays)
            console.log(cql);
            newlayerdialog.dialog("close");

        }
    }

    var newlayerdialog = $("#dialog-newlayer").dialog({
        autoOpen: false,
        modal: true,
        width: 800,
        height: 600,
        buttons: {
            "Agregar capa": agregarCapa,
            "Cancelar": function () {
                newlayerdialog.dialog("close");
            }
        },
        close:

            function () {
                $("#newlayerform")[0].reset();
                $("#newlayeradvaced")[0].reset();
                $("#newlayerstyle")[0].reset();
                $("#id_entidad").val(null).trigger('change');
                $("#id_municipio").val(null).trigger('change');
                $("#id_clase_roca").val(null).trigger('change');
                $("#id_tipo_roca").val(null).trigger('change');
                $("#id_tipo_suelo").val(null).trigger('change');
                $("#id_uso_suelo").val(null).trigger('change');
                $("#newtextadvanced").val(null).trigger('change');
                $("#newtextadvanced").val(null).trigger('change');
            }
    });

    $("#agregarcapa").on("click", function () {
        console.log("agregar capa")
        newlayerdialog.dialog("open")
        console.log("luego del dialog")

    });

    var colormap = null

    $("#id_colormap").change(function () {

        $.ajax('/suelos/styles/images/' + $("#id_colormap").val()).done(function (data) {

            // si hay un estilo seleccionado:
            if ($("#id_colormap").val() > 0) {
                // /suelos/styles/polygon.sld
                console.log($("#id_colormap").val())

                color = jQuery.parseJSON(data)[0].fields
                console.log(color)
                console.log(color.colormap_continuous)
                console.log(color.colormap_discrete)
                if (color.colormap_continuous != "" && color.colormap_discrete != "") {
                    $("#samplecolormap").html('<img width="100%" src="/media/' + color.colormap_continuous + '"><img width="100%" src="/media/' + color.colormap_discrete + '">')
                    console.log('<img width="100%" src="/media/' + color.colormap_continuous + '"><img width="100%" src="/media/' + color.colormap_discrete + '">')
                }
                if (color.colormap_continuous != "" && color.colormap_discrete == "") {
                    $("#samplecolormap").html('<img width="100%" src="/media/' + color.colormap_continuous + '">')
                }
                if (color.colormap_continuous == "" && color.colormap_discrete != "") {
                    $("#samplecolormap").html('<img width="100%" src="/media/' + color.colormap_discrete + '">')
                }
            } else {
                $("#samplecolormap").html('')
            }
        })

    });


    var controles = L.control.layers(baseLayers, overlays);

    controles.addTo(map);


    L.control.zoom({
        position: 'topright'
    }).addTo(map);

})