# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json


class WebsiteMap(http.Controller):
    @http.route('/map/geojson/points.geojson', type='http', auth="user", methods=['GET'], website=True)
    def get_goajson_locattions(self, **kw):
        res = []
        data = request.env['res.partner'].search(
            [('partner_latitude', '!=', 0)]
        )

        for d in data:
            coll_html = "<p>Partner: {name}</p>".format(name=d.display_name)

            if d.country_id.name == 'Belgium':
                status_color = 'red'
            elif d.country_id.name == 'France':
                status_color = 'yellow'
            else:
                status_color = 'green'
            item = {
                "geometry": {
                    "type": "Point",
                    "coordinates":
                        [round(d.partner_longitude, 5),
                         round(d.partner_latitude, 5)]
                },
                "type": "Feature",
                "properties": {
                    "popupContent": unicode(coll_html, "utf-8"),
                    "status": status_color
                },
                "id": d.id
            }
            res.append(item)
        if len(res) > 0:
            res = {"type": "FeatureCollection", "features": res}
        else:
            return "raise error"
        return json.dumps(res)
