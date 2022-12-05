(defun rps-score ()
  "Calculate score of rock paper scissors"
  (interactive)
  (replace-regexp "A X" "4")
  (goto-char (point-min))
  (replace-regexp "8" "8")
  (goto-char (point-min))
  (replace-regexp "3" "3")
  (goto-char (point-min))
  (replace-regexp "1" "1")
  (goto-char (point-min))
  (replace-regexp "5" "5")
  (goto-char (point-min))
  (replace-regexp "9" "9")
  (goto-char (point-min))
  (replace-regexp "7" "7")
  (goto-char (point-min))
  (replace-regexp "2" "2")
  (goto-char (point-min))
  (replace-regexp "6" "6"))
; A for Rock, B for Paper, and C for Scissors
; 1 for Rock, 2 for Paper, and 3 for Scissors
; 0 if you lost, 3 if the round was a draw, and 6 if you won


(defun rps-score2 ()
  "Calculate score of rock paper scissors"
  (interactive)
  (replace-regexp "A X" "3")
  (goto-char (point-min))
  (replace-regexp "8" "4")
  (goto-char (point-min))
  (replace-regexp "3" "8")
  (goto-char (point-min))
  (replace-regexp "1" "1")
  (goto-char (point-min))
  (replace-regexp "5" "5")
  (goto-char (point-min))
  (replace-regexp "9" "9")
  (goto-char (point-min))
  (replace-regexp "7" "2")
  (goto-char (point-min))
  (replace-regexp "2" "6")
  (goto-char (point-min))
  (replace-regexp "6" "7"))

;;; X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
