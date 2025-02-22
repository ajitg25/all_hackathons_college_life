const {
  Client,
  defaultAxiosInstance,
} = require("@googlemaps/google-maps-services-js");
const router = require("express").Router();
const client = new Client({});

router.post("/location", (req, res) => {
  const location = req.body.post_code;
  let latLong = {};
  client
    .geocode(
      {
        params: {
          components: "country:CA|postal_code:" + location,
          key: "AIzaSyB6avRdS_ypWuB6gYLcz0tX9GHdzg5iD3U",
        },
        timeout: 1000,
      },
      defaultAxiosInstance
    )
    .then((response) => res.send(response.data));
});

module.exports = router;
