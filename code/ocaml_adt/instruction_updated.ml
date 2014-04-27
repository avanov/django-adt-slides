type instruction =
   | Order of order
   | Cancel of cancel
   | Cancel_replace of cancel_replace
