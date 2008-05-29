// Autogenerated AST node
package org.python.antlr.ast;
import org.python.antlr.PythonTree;
import org.antlr.runtime.Token;
import java.io.DataOutputStream;
import java.io.IOException;

public class ClassDef extends stmtType {
    public String name;
    public exprType[] bases;
    public stmtType[] body;

    public static final String[] _fields = new String[] {"name","bases","body"};

    public ClassDef(PythonTree tree, String name, exprType[] bases, stmtType[]
    body) {
        super(tree);
        this.name = name;
        this.bases = bases;
        if (bases != null) {
            for(int ibases=0;ibases<bases.length;ibases++) {
                addChild(bases[ibases]);
            }
        }
        this.body = body;
        if (body != null) {
            for(int ibody=0;ibody<body.length;ibody++) {
                addChild(body[ibody]);
            }
        }
    }

    public String toString() {
        return "ClassDef";
    }

    public <R> R accept(VisitorIF<R> visitor) throws Exception {
        return visitor.visitClassDef(this);
    }

    public void traverse(VisitorIF visitor) throws Exception {
        if (bases != null) {
            for (int i = 0; i < bases.length; i++) {
                if (bases[i] != null)
                    bases[i].accept(visitor);
            }
        }
        if (body != null) {
            for (int i = 0; i < body.length; i++) {
                if (body[i] != null)
                    body[i].accept(visitor);
            }
        }
    }

    public int getLineno() {
        return getLine();
    }

    public int getCol_offset() {
        return getCharPositionInLine();
    }

}
