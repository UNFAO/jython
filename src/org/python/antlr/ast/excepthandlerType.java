// Autogenerated AST node
package org.python.antlr.ast;
import org.python.antlr.PythonTree;
import org.python.antlr.ListWrapper;
import org.antlr.runtime.CommonToken;
import org.antlr.runtime.Token;
import java.io.DataOutputStream;
import java.io.IOException;

public class excepthandlerType extends PythonTree {
    private exprType excepttype;
    public exprType getInternalExcepttype() {
        return excepttype;
    }
    public void setExcepttype(exprType excepttype) {
        this.excepttype = excepttype;
    }

    private exprType name;
    public exprType getInternalName() {
        return name;
    }
    public void setName(exprType name) {
        this.name = name;
    }

    private ListWrapper<stmtType> body;
    public ListWrapper<stmtType> getInternalBody() {
        return body;
    }
    public void setBody(java.util.List<stmtType> body) {
        this.body = new ListWrapper<stmtType>(body);
    }

    private int lineno;
    public int getInternalLineno() {
        return lineno;
    }
    public void setLineno(int lineno) {
        this.lineno = lineno;
    }

    private int col_offset;
    public int getInternalCol_offset() {
        return col_offset;
    }
    public void setCol_offset(int col_offset) {
        this.col_offset = col_offset;
    }


    private final static String[] fields = new String[] {"excepttype", "name",
                                                          "body", "lineno",
                                                          "col_offset"};
    public String[] get_fields() { return fields; }

    public excepthandlerType(exprType excepttype, exprType name,
    java.util.List<stmtType> body, int lineno, int col_offset) {
        this.excepttype = excepttype;
        addChild(excepttype);
        this.name = name;
        addChild(name);
        this.body = new ListWrapper<stmtType>(body);
        if (body != null) {
            for(PythonTree t : body) {
                addChild(t);
            }
        }
        this.lineno = lineno;
        this.col_offset = col_offset;
    }

    public excepthandlerType(Token token, exprType excepttype, exprType name,
    java.util.List<stmtType> body, int lineno, int col_offset) {
        super(token);
        this.excepttype = excepttype;
        addChild(excepttype);
        this.name = name;
        addChild(name);
        this.body = new ListWrapper<stmtType>(body);
        if (body != null) {
            for(PythonTree t : body) {
                addChild(t);
            }
        }
        this.lineno = lineno;
        this.col_offset = col_offset;
    }

    public excepthandlerType(int ttype, Token token, exprType excepttype,
    exprType name, java.util.List<stmtType> body, int lineno, int col_offset) {
        super(ttype, token);
        this.excepttype = excepttype;
        addChild(excepttype);
        this.name = name;
        addChild(name);
        this.body = new ListWrapper<stmtType>(body);
        if (body != null) {
            for(PythonTree t : body) {
                addChild(t);
            }
        }
        this.lineno = lineno;
        this.col_offset = col_offset;
    }

    public excepthandlerType(PythonTree tree, exprType excepttype, exprType
    name, java.util.List<stmtType> body, int lineno, int col_offset) {
        super(tree);
        this.excepttype = excepttype;
        addChild(excepttype);
        this.name = name;
        addChild(name);
        this.body = new ListWrapper<stmtType>(body);
        if (body != null) {
            for(PythonTree t : body) {
                addChild(t);
            }
        }
        this.lineno = lineno;
        this.col_offset = col_offset;
    }

    public String toString() {
        return "excepthandler";
    }

    public String toStringTree() {
        StringBuffer sb = new StringBuffer("excepthandler(");
        sb.append("excepttype=");
        sb.append(dumpThis(excepttype));
        sb.append(",");
        sb.append("name=");
        sb.append(dumpThis(name));
        sb.append(",");
        sb.append("body=");
        sb.append(dumpThis(body));
        sb.append(",");
        sb.append("lineno=");
        sb.append(dumpThis(lineno));
        sb.append(",");
        sb.append("col_offset=");
        sb.append(dumpThis(col_offset));
        sb.append(",");
        sb.append(")");
        return sb.toString();
    }

    public <R> R accept(VisitorIF<R> visitor) throws Exception {
        traverse(visitor);
        return null;
    }

    public void traverse(VisitorIF visitor) throws Exception {
        if (excepttype != null)
            excepttype.accept(visitor);
        if (name != null)
            name.accept(visitor);
        if (body != null) {
            for (PythonTree t : body) {
                if (t != null)
                    t.accept(visitor);
            }
        }
    }

}
