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

    var suelos = L.tileLayer.betterWms('http://localhost:8080/geoserver/ENES/ows?', {
        layers: 'ENES:suelos_suelo',
        tiled: true,
        format: 'image/png',
        transparent: true,
        minZoom: 5,
        maxZoom: 22,
    }).addTo(map);

    var suelos2 = L.tileLayer.betterWms('http://localhost:8080/geoserver/ENES/ows?', {
        layers: 'ENES:suelos_suelo',
        tiled: true,
        format: 'image/png',
        transparent: true,
        minZoom: 5,
        maxZoom: 22,
    })

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

    var overlays = {
        //"Suelos <a href=\"#\" onclick=\"alert(); alert(2);\">je</a>": suelos,
        "Suelos": suelos,
    };

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

    function checkLength(o, n, min, max) {
        if (o.val().length > max || o.val().length < min) {
            o.addClass("ui-state-error");
            updateTips("Length of " + n + " must be between " +
                min + " and " + max + ".");
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
            overlays[$("#nombre").val()] = suelos2
            suelos2.addTo(map)
            controles.remove(map)
            //controles.addTo(map);


            console.log(overlays)
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
                $("#layerform")[0].reset()
                $("#id_entidad").val(null).trigger('change');
                $("#id_municipio").val(null).trigger('change');
                $("#id_clase_roca").val(null).trigger('change');
                $("#id_tipo_roca").val(null).trigger('change');
                $("#id_tipo_suelo").val(null).trigger('change');
                $("#id_uso_suelo").val(null).trigger('change');
            }
    });

    $("#agregarcapa").on("click", function () {
        console.log("agregar capa")
        newlayerdialog.dialog("open")
        console.log("luego del dialog")

    });


    //overlays["otro"] = suelos;

    var controles = L.control.layers(baseLayers, overlays);

    controles.addTo(map);


    L.control.zoom({
        position: 'topright'
    }).addTo(map);

})