type order = { id: int; price: float; size: int; }
type cancel = { xid: int; }

type instruction =
   | Order of order
   | Cancel of cancel

let filter_by_oid instructions oid =
    List.filter instructions
        (fun x -> match x with
                  | Order o -> o.id = oid
                  | Cancel c -> c.xid = oid)
     ;;
