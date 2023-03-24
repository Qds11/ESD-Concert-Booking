paypal.Buttons({
    style : {
        color: 'white',
        shape: 'pill'
    },
    createOrder: function (data, actions) { // details of transaction
        return actions.order.create({
            purchase_units : [{
                amount: {
                    value: '0.1'
                }
            }]
        });
    },
    onApprove: function (data, actions) {
        return actions.order.capture().then(function (details) {
            console.log(details)
            window.location.replace("http://localhost/esd/ESD-Concert-Booking/backend/payment/success.php")
            // call notif directly 
        })
    },
    onCancel: function (data) {
        window.location.replace("http://localhost/esd/ESD-Concert-Booking/backend/payment/Oncancel.php")
    }
  }).render('#paypal-payment-button');

<script>import NavBar from "@/components/shared/NavBar.vue";</script>