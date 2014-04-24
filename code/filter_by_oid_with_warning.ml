let filter_by_oid instructions oid =
    List.filter instructions
        (fun x -> match x with
                  | Order o -> o.id = oid
                  | Cancel c -> c.xid = oid)
    ;;

(* Warning P: This pattern-matching is not exhaustive
Here is an example of a value that is not matched... *)
